from django.db import models

class Position(models.Model):
    position_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'positions'

    def __str__(self):
        return self.position_name

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    nationality = models.CharField(max_length=100)
    age = models.IntegerField()
    wage = models.IntegerField()
    shirt_number = models.IntegerField()
    is_active = models.BooleanField(default=True)
    joined_date = models.DateField()

    class Meta:
        db_table = 'players'

    def __str__(self):
        return self.name

class Match(models.Model):
    opponent = models.CharField(max_length=100)
    match_date = models.DateField()
    home_or_away = models.CharField(max_length=10)
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()
    competition = models.CharField(max_length=100)

    class Meta:
        db_table = 'matches'

    def __str__(self):
        return f"vs {self.opponent} ({self.match_date})"

class PlayerStat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        db_table = 'player_stats'

    def __str__(self):
        return f"{self.player.name} vs {self.match.opponent}"