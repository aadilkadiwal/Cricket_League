from django.urls import path
from . import views

urlpatterns = [
    path('', views.matches, name = 'matches'),
    path('teams/', views.teams, name = 'teams'),
    path('players/', views.players, name = 'players')
]