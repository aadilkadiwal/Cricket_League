from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView
from .models import Match, Team, Player, Venue


def matches(request):
    context = {
        'matchs' : Match.objects.all()
    }
    return render(request, 'tournament/matches.html',context)

class MatchDetailView(DetailView):
    model = Match
    template_name = 'tournament/result.html'  

def teams(request):
    context = {
        'teams' : Team.objects.all()
    }
    return render(request, 'tournament/teams.html',context)    

class TeamPlayerDetailView(DetailView):
    model = Team
    template_name = 'tournament/team.html'

def players(request):
    context = {
        'players' : Player.objects.all()
    }
    return render(request, 'tournament/players.html', context)   

class PlayerProfileDetailView(DetailView):
    model = Player  
    template_name = 'tournament/profile.html'   

def venues(request):
    context = {
        'venues' : Venue.objects.all()
    }
    return render(request, 'tournament/venues.html', context)

class VenueDetailView(DetailView):
    model = Venue
    template_name = 'tournament/venue.html'

def score(request):
    context = {
        'teams' : Team.objects.all()
    }
    return render(request, 'tournament/score.html', context)  