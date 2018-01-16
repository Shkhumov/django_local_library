from django.contrib import admin
from  my_site.apps.home.models import Article ,Contact , Article_two, Posts, Reclama

# Register your models here.

admin.site.register(Article)
admin.site.register(Article_two)
admin.site.register(Contact)
admin.site.register(Posts)
admin.site.register(Reclama)