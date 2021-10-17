from django.shortcuts import render
from .models import Match
from .models import Team
from .models import Player

def matches(request):
    context = {
        'matchs' : Match.objects.all()
    }
    return render(request, 'tournament/matches.html',context)

def teams(request):
    context = {
        'teams' : Team.objects.all()
    }
    return render(request, 'tournament/teams.html',context)    

def players(request):
    context = {
        'players' : Player.objects.all()
    }
    return render(request, 'tournament/players.html', context)    