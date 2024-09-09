from django.db import models

class Project(models.Model):
    owner = models.CharField(max_length=40)
    repo_name = models.CharField(max_length=40)
    last_info_update = models.DateTimeField("last info update")
    avatar = models.ImageField(upload_to='images/', null=True, blank=True)
