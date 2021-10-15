from django.shortcuts import render

def matches(request):
    return render(request, 'tournament/matches.html')

def team(request):
    return render(request, 'tournament/team.html')    