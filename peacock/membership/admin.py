
# Register your models here.
from django.contrib import admin

from .models import Member, Contribution

admin.site.register(Member)
admin.site.register(Contribution)
