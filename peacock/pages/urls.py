from django.urls import path

from . import views

urlpatterns = [
    path("<page_slug>/", views.page, name="page"),
]
