from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from my_site.apps.callback.models import Callback
from my_site.apps.callback.forms import CallbackForm
# Create your views here.

def add_callback(request):
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
    else:
        form = CallbackForm()
    return HttpResponseRedirect('/')