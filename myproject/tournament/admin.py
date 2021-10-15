from django.contrib import admin
from .models import Country
from .models import Venue
from .models import Team
from .models import Player
from .models import Match
from .models import MatchSummary

admin.site.register(Country)
admin.site.register(Venue)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(MatchSummary)