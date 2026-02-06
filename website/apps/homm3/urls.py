from django.urls import path
from . import api

app_name='homm3'
urlpatterns = [
    path('api/players', api.GetAllPlayers.as_view(), name='get_players'),
    path('api/player/create', api.CreatePlayer.as_view(), name='create_player'),
]