from django.conf.urls import patterns, url, include

from rest_framework import routers

from songs import views as songs_views
#from auth import views as auth_views


router = routers.DefaultRouter()
router.register(r'songs', songs_views.SongCreateReadView)
#router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns("",
    # Router for testing
    url(r'^router/', include(router.urls)),
    # url api:songs
    url(
        regex = r'^songs/$',
        view = songs_views.SongCreateReadView.as_view(),
        name = "songs"
    ),
    # url api:songs song.slug
    url(
        regex = r'^songs/(?P<slug>[-\w]+)/$',
        view = songs_views.SongReadUpdateDeleteView.as_view(),
        name = "songs"
    ),

   )