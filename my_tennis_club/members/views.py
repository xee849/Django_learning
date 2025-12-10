from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members
# Create your views here.

def member(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))
