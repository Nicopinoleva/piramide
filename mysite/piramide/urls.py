from django.urls import path

from .views import *

urlpatterns = [
    path('', Start.as_view(), name='start_url'),
    path('<int:game_id>', AddPlayers.as_view(), name='add_players_url'),
    path('<int:game_id>/start', StartGame.as_view(), name='start_game_url'),
    path('<int:game_id>/<str:player_name>', DeletePlayer.as_view(), name='delete_player_url')
]