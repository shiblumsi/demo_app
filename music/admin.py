from django.contrib import admin
from .models import Album, Artist, Song, Playlist
# Register your models here.


@admin.register(Artist)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'description', 'photo')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist', 'title', 'cover', 'release_date')


@admin.register(Song)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist', 'album', 'title', 'audio_file', 'duration')



admin.site.register(Playlist)
#ManyToMany Field not working Modeladmin
# class AlbumAdmin(admin.ModelAdmin):    
#     list_display = ('id', 'user', 'name', 'songs')