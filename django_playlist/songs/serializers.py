from rest_framework import serializers
from .models import Playlist, Song


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('name', 'playlist', 'url')


class PlaylistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = Playlist
        fields = ('title', 'user', 'songs' 'id')