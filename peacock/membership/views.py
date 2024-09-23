from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
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

def profile(request, username):
    member = get_object_or_404(Member, username=username)
    return render(request, "membership/profile.html", {"member": member})
    
