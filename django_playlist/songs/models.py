from django.db import models
from django.utils import timezone

from auth.models import User
# Create your models here.

class Playlist(models.Model):
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created', default=timezone.now())
    user = models.FoerignKey(User)

    def __unicode__(self):
        return self.title

class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    playlist = models.ForeignKey(Playlist)

    def __unicode__(self):
        return (self.name + " - " + self.artist)