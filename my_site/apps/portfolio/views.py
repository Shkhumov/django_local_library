from django.http import HttpResponse
from django.shortcuts import render
from my_site.apps.portfolio.models import Photo, Album

# Create your views here.
def portfolio(request):
    albums = Album.objects.all()
    photos = Photo.objects.all()
    contex = {
        "photos": photos,
        "albums": albums,

    }
    return  render(request, "portfolio.html", contex)

