from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=40, primary_key=True)
    html_url = models.URLField()
    avatar_url = models.URLField()
    gh_id = models.PositiveIntegerField()
    last_info_update = models.DateTimeField()

class Project(models.Model):
    full_name = models.CharField(max_length=40, primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    repo_name = models.CharField(max_length=40)
    html_url = models.URLField()
    description = models.CharField(max_length=1000)
    gh_id = models.PositiveIntegerField()
    last_info_update = models.DateTimeField()
