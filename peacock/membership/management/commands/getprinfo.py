from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from membership.models import Member, Contribution
from projects.models import Project

import os, json

import requests

class Command(BaseCommand):
    help = "Get contribution information from GitHub for all members"

    def handle(self, *args, **options):

        with open("projects.txt", "r") as file:
            repos = file.read().split()

        headers = {"Authorization": os.environ["GH_TOKEN"]}

        for member in Member.objects.all():
            url = f'https://api.github.com/search/issues?q=type:pr+author:{member.github_handle}&per_page=100'
            while url is not None:
                res = requests.get(url, headers=headers)
                # set url to the next page, or None is no next page
                url = None
                for link in res.headers["Link"].split(","):
                    parts = link.strip().split(";")
                    if parts[1].strip() == 'rel="next"':
                        url = parts[0].strip("<").strip(">")
                # parse and handle results
                prs_json = json.loads(res.text)["items"]
                for pr in prs_json:
                    repo = "/".join(pr["repository_url"].split("/")[-2:])
                    id = "/".join(pr["html_url"].split("/")[-4:])
                    if repo in repos:
                        pr_obj = list(Contribution.objects.filter(gh_id=pr["id"]))
                        if len(pr_obj) != 0:
                            obj = pr_obj[0]
                            obj.title = pr["title"]
                            obj.state = pr["state"]
                            obj.merged_at = pr.get("merged_at", None)
                            obj.save()
                        else:
                            obj = Contribution.objects.create(
                                id = id,
                                gh_id = pr["id"],
                                author = member,
                                html_url = pr["html_url"],
                                repo = Project.objects.get(full_name=repo),
                                title = pr["title"],
                                state = pr["state"],
                                created_at = pr["created_at"],
                                merged_at = pr.get("merged_at", None)
                            )
                            obj.save()
