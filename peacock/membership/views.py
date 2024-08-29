from django.http import HttpResponse
from django.template import loader
from .models import Member


def index(request):
    template = loader.get_template("membership/index.html")
    members = Member.objects.all()
    member_0 = members[0]
    for d in dir(member_0):
        print(d)
    context = {"members" : members
    }

    return HttpResponse(template.render(context, request))