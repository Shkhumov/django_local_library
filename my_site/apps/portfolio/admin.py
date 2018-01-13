from django.contrib import admin
from my_site.apps.portfolio.models import Photo, Album


class ImageAdmin(admin.ModelAdmin):
    admin.site.disable_action('delete_selected')
    def full_delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()
    full_delete_selected.short_description = 'Удалить выбранные иллюстрации'
    actions = ['full_delete_selected']
    list_display = ('title', 'captions', 'get_mini_html')

class ProjectImageInline(admin.StackedInline):
    model = Photo
    max_num=10
    extra=0

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline,]

admin.site.register(Photo ,ImageAdmin)
admin.site.register(Album, ProjectAdmin)


