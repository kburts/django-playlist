from django.contrib import admin
from .models import Playlist, Song

# Register your models here.

class SongInline(admin.TabularInline):
    model = Song
    extra = 3

class PlaylistAdmin(admin.ModelAdmin):
    '''
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['creation_date'], 'classes':['collapse']}),
    ]
    inlines = [SongInline]
    list_display = ('playlist', 'creation_date', 'user')
    list_filter = ['pub_date']
    search_fields = ['playlist']
    '''
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('User information', {'fields': ['user']}),
        ('Date information', {'fields': ['creation_date'], 'classes': ['collapse']}),
    ]
    inlines = [SongInline]
    list_display = ('title', 'creation_date', 'user')
    list_filter = ['creation_date']
    search_fields = ['title']

admin.site.register(Playlist, PlaylistAdmin)
#admin.site.register(Song)