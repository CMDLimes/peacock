

# name
# email
# social media urls: linkedin, mastodon, twitter (optional)
# bio: markdown (optional)
# avatar: (optional)
# pronouns (optional)
# location (?)
# List of projects. (optional for now)
# GitHub handle: connect with GitHub API.
# confirmed status: whether email address is confirmed
# approval status: whether approved by us. (True false)
# approved by: the username of the admin who approved
from django.contrib.auth.models import AbstractUser
from django.db import models

class Member(AbstractUser):
    twitter_url = models.CharField(max_length=100)
