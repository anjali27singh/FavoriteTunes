# TuneTracker/urls.py
from django.urls import path
from .views import song_list, song_detail
from .views import playlist_view


urlpatterns = [
    path('', song_list, name='song_list'),
    path('song/<int:song_id>/', song_detail, name='song_detail'),
    path('playlist/', playlist_view, name='playlist'),

]




