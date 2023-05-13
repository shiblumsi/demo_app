from django.urls import path
from . import views

urlpatterns = [
    #path('',views.home),
    #path('',views.querys),
    #path('',views.get_album_song_by_user),
    path('<int:pk>', views.song_create, name='song-create'),
    path('',views.playlist)
]
