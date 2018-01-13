from django.http import HttpResponse
from django.shortcuts import render
from my_site.apps.aboutus.models import About


def abouts(request):
    abouts = About.objects.all()
    contex = {
        "abouts": abouts
    }
    return  render(request, "about.html", contex)