from django.http import HttpResponse
from django.shortcuts import render
from my_site.apps.home.models import Article, Article_two, Contact, Posts, Reclama


# Create your views here.
def index(request):
    articls = Article.objects.all()
    articls2 = Article_two.objects.all()
    contacts = Contact.objects.all()
    posts = Posts.objects.all()
    reclams = Reclama.objects.all()

    contex = {
        "articls": articls ,
        "articls2": articls2,
        "contacts": contacts,
        "posts": posts,
        "reclams": reclams,

    }
    return  render(request, "index.html", contex)



