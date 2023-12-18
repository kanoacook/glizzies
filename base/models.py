from django.db import models
from django.contrib.auth.models import User
import json

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sleeper_id = models.CharField(max_length=200, null=True, blank=True)
    sleeper_team_name = models.CharField(max_length=200, null=True, blank=True)
    sleeper_display_name = models.CharField(max_length=200, null=True, blank=True)
    sleeper_league_id = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    sleeper_avatar = models.CharField(max_length=250, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)


    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.sleeper_team_name

    def save(self, *args, **kwargs):
        if self.user:
            self.user.first_name = self.first_name
            self.user.last_name =  self.last_name
            self.user.save()  # Save the User instance
        super(UserProfile, self).save(*args, **kwargs)



class NFLPlayers(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    search_first_name = models.CharField(max_length=100, blank=True, null=True)
    search_last_name = models.CharField(max_length=100, blank=True, null=True)
    team = models.CharField(max_length=3, blank=True, null=True)  # Assuming NFL team codes are 3 letters
    fantasy_positions = models.JSONField(blank=True, null=True)  # JSONField to store list of positions
    stats_id = models.IntegerField(blank=True, null=True)
    yahoo_id = models.IntegerField(blank=True, null=True)
    player_id = models.CharField(max_length=50, unique=True)  # Assuming player_id is a unique identifier
    espn_id = models.IntegerField(blank=True, null=True)
    oddsjam_id = models.CharField(max_length=100, blank=True, null=True)
    gsis_id = models.CharField(max_length=100, blank=True, null=True)
    sportradar_id = models.CharField(max_length=100, blank=True, null=True)
    rotowire_id = models.IntegerField(blank=True, null=True)
    rotoworld_id = models.IntegerField(blank=True, null=True)
    pandascore_id = models.IntegerField(blank=True, null=True)
    fantasy_data_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.team})"

    def save(self, *args, **kwargs):
        # Custom save method to handle JSON fields
        if isinstance(self.fantasy_positions, list):
            self.fantasy_positions = json.dumps(self.fantasy_positions)
        super(NFLPlayers, self).save(*args, **kwargs)