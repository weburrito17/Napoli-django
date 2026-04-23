from django.contrib import admin
from .models import Position, Player, Match, PlayerStat

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['position_name']

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'nationality', 'age', 'wage', 'shirt_number', 'is_active']

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['opponent', 'match_date', 'home_or_away', 'goals_for', 'goals_against', 'competition']

@admin.register(PlayerStat)
class PlayerStatAdmin(admin.ModelAdmin):
    list_display = ['player', 'match', 'goals', 'assists', 'minutes_played', 'rating']