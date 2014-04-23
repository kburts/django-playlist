from rest_framework import generics, permissions
from .models import Playlist, Song
from .serializers import PlaylistSerializer, SongSerializer
from django.shortcuts import render


class PlaylistList(generics.ListCreateAPIView):
    model = Playlist
    serializer_class = PlaylistSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PlaylistDetail(generics.RetrieveAPIView):
	model = Playlist
	serializer_class = PlaylistSerializer
	lookup_url_kwarg = 'question_pk'
	permission_classes = [
		permissions.AllowAny
	]

class SongUpdate(generics.UpdateAPIView):
	model = Song
	serializer_class = SongSerializer
	lookup_url_kwarg = 'choice_pk'
	permission_classes = [
		permissions.AllowAny
	]

class SongList(generics.ListCreateAPIView):
    model = Song
    serializer_class = SongSerializer
    permission_classes = [
        permissions.AllowAny
    ]
