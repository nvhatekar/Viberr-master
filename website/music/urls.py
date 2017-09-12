from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/album_id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album_add'),

    # music/album/id/update
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album_update'),

    # music/album/id/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album_delete'),

    #music/album/addsong
    url(r'^album/(?P<pk>[0-9]+)/addsong/$', views.SongCreate.as_view(), name='song_add'),

]