from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='artists/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True,verbose_name='artist_user') #In model show verbos_name

    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='albums/', null=True, blank=True)
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,related_name='singer')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, help_text='song name')
    audio_file = models.FileField(upload_to='songs/')
    duration = models.FloatField()

    def __str__(self):
        return f'{self.title}---> {self.artist}'

class Playlist(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, related_name='playlists', blank=True)

    def __str__(self):
        return self.name