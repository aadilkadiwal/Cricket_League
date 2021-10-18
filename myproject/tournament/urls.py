from django.urls import path
from . import views 

urlpatterns = [
    path('', views.matches, name = 'matches'),
    path('teams/', views.teams, name = 'teams'),
    path('players/', views.players, name = 'players'),
    path('score/', views.score, name = 'score'),
    path('venues/', views.venues, name = 'venues'),
    path('teams/<int:pk>', views.TeamPlayerDetailView.as_view(), name = 'team-detail'),
    path('players/<int:pk>', views.PlayerProfileDetailView.as_view(), name = 'player-detail'),
    path('matches/<int:pk>', views.MatchDetailView.as_view(), name = 'match-detail'),
    path('venues/<int:pk>', views.VenueDetailView.as_view(), name = 'venue-detail'),
]