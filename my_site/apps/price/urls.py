from django.conf.urls import url
from django.contrib import admin
from my_site.apps.price import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^price/$', views.price, name='price'),
    url(r'^prise/add/$', views.add_price, name='add_price'),

]
