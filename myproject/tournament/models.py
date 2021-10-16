from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=30)
    flag = models.ImageField(default='default.jpg', upload_to='Country')

    def __str__(self):
        return self.name

class Venue(models.Model):   
    stadium_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    country = models.ForeignKey(Country, related_name='venues', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.stadium_name

class Team(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(default='default.jpg', upload_to='Team_logo')
    country = models.ForeignKey(Country, related_name='teams', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Player(models.Model):

    class Role(models.TextChoices):
        batsman = 'Batsman'
        bowler = 'Bowler'
        all_rounder = 'All Rounder'

    name = models.CharField(max_length=30)
    picture = models.ImageField(default='default.jpg', upload_to='Player_pic')
    team = models.ForeignKey(Team, related_name='players', on_delete=models.DO_NOTHING)
    dob = models.DateField()
    birth_place = models.ForeignKey(Country, related_name='players', on_delete=models.DO_NOTHING)
    role = models.CharField(max_length=11, choices=Role.choices, default=Role.all_rounder)

    def __str__(self):
        return self.name
    
class Match(models.Model):
    time = models.DateTimeField()
    team1 = models.ForeignKey(Team, related_name='matchs', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, related_name='matchs', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.time

class MatchSummary(models.Model):
    match_detail = models.ForeignKey(Match, related_name='matchsummarys', on_delete=models.CASCADE)
    match_winner = models.ForeignKey(Team, related_name='matchsummarys', on_delete=models.CASCADE)
    match_looser = models.ForeignKey(Team, on_delete=models.CASCADE)
    man_of_the_match = models.ForeignKey(Player, related_name='matchsummarys', on_delete=models.DO_NOTHING)
    bowler_of_the_match = models.ForeignKey(Player, related_name='bowler', on_delete=models.DO_NOTHING)
    best_fielder = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
 
    def __str__(self):
        return self.match_detail