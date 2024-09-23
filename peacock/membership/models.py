

# name
# email
# social media urls: linkedin, mastodon, twitter (optional)
# bio: markdown (optional)
# avatar: (optional)
# pronouns (optional)
# location (?)
# List of projects. (optional for now) **imprement later**
# GitHub handle: connect with GitHub API.
# confirmed status: whether email address is confirmed
# approval status: whether approved by us. (True false)
# approved by: the username of the admin who approved
from django.contrib.auth.models import AbstractUser
from django.db import models
from projects.models import Project

class Member(AbstractUser):
    website_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    mastodon_url = models.URLField(null=True, blank=True)
    bio = models.CharField(max_length=1000, null=True, blank=True)
    avatar = models.ImageField(upload_to='images/', null=True, blank=True)
    pronouns = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    github_handle = models.CharField(max_length=40)
    confirmed_status = models.BooleanField(default = False)
    approved_status = models.BooleanField(default = False)
    approved_by = models.CharField(max_length=40, null=True, blank=True)

class Contribution(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    gh_id = models.PositiveIntegerField()
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    html_url = models.URLField()
    repo = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    state = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    merged_at = models.DateTimeField(null=True, blank=True)
