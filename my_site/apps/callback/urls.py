from django.conf.urls import url
from django.contrib import admin
from my_site.apps.callback import views



urlpatterns = [
    url(r'^add/callback/$', views.add_callback, name='add_callback'),

]