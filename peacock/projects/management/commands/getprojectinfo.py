from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from projects.models import Owner, Project

import os, json

import requests

class Command(BaseCommand):
    help = "Get project information from GitHub"

    def handle(self, *args, **options):

        with open("projects.txt", "r") as file:
            repos = file.read().split()

        headers = {"Authorization": os.environ["GH_TOKEN"]}

        for repo in repos:
            url = "https://api.github.com/repos/" + repo
            res = requests.get(url, headers=headers)
            repo_json = json.loads(res.text)
            # create owner object
            owner_json = repo_json["owner"]
            owner_obj = list(Owner.objects.filter(name=owner_json["login"]))
            if len(owner_obj) != 0:
                obj = owner_obj[0]
                obj.html_url=owner_json["html_url"]
                obj.avatar_url = owner_json["avatar_url"]
                obj.last_info_update = timezone.now()
                obj.save()
                print(f"Owner object ({owner_json["login"]}) updated.")
            else:
                obj = Owner.objects.create(
                    name=owner_json["login"],
                    html_url=owner_json["html_url"],
                    avatar_url = owner_json["avatar_url"],
                    gh_id = owner_json["id"],
                    last_info_update = timezone.now()
                )
                obj.save()
                print(f"Owner object ({owner_json["login"]}) created.")

            # create project object

            repo_obj = list(Project.objects.filter(gh_id=repo_json["id"]))

            if len(repo_obj) != 0:
                pobj = repo_obj[0]
                pobj.full_name = repo_json["full_name"]
                pobj.owner = obj
                pobj.repo_name = repo_json["name"]
                pobj.html_url = repo_json["html_url"]
                pobj.description = repo_json["description"]
                pobj.last_info_update = models.DateTimeField("last info update")
                pobj.save()
                print(f"Project object ({repo_json["full_name"]}) updated.")
            else:
                pobj = Project.objects.create(
                    full_name = repo_json["full_name"],
                    owner = obj,
                    repo_name = repo_json["name"],
                    html_url = repo_json["html_url"],
                    description = repo_json["description"],
                    gh_id = repo_json["id"],
                    last_info_update = timezone.now()
                )
                pobj.save()
                print(f"Project object ({repo_json["full_name"]}) created.")
