from django.conf.urls import patterns, url

from .views import PlaylistList, PlaylistDetail, SongList, SongUpdate

urlpatterns = patterns('songs.views',
	url(r'^playlists$', PlaylistList.as_view(), name='playlists_list'),
	url(r'^playlists/(?P<playlist_pk>[0-9]+)/$', PlaylistDetail.as_view(),
			name="playlist_detail"),
	url(r'^songs$', SongList.as_view(), name='songs_list'),
	url(r'^songs/(?P<song_pk>[0-9]+)/$', SongUpdate.as_view(),
			name='songs_update'),
)