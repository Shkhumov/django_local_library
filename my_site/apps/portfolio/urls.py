from django.conf.urls import url, include
from django.contrib import admin
from  my_site.apps.portfolio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^portfolio/$', views.portfolio, name='portfolio'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)