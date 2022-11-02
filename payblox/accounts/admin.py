from django.contrib import admin

from .models import User,Item,Song

class SongAdmin(admin.ModelAdmin):
    list_display = ['name','get_all_singers']

admin.site.register(User)
admin.site.register(Item)
admin.site.register(Song,SongAdmin)
