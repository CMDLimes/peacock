from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=40)
    html_url = models.URLField()
    avatar = models.ImageField(upload_to='images/', null=True, blank=True)
    gh_id = models.PositiveIntegerField()
    last_info_update = models.DateTimeField("last info update")

class Project(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    repo_name = models.CharField(max_length=40)
    html_url = models.URLField()
    description = models.CharField(max_length=1000)
    last_info_update = models.DateTimeField("last info update")
    gh_id = models.PositiveIntegerField()
    last_info_update = models.DateTimeField("last info update")
