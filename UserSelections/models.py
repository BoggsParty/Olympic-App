from django.db import models

class UserSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='none')
    gold_medal_winner = models.ForeignKey('CountryInfo.Country', blank=True, null=True, related_name='gold_medal_winner+')
    silver_medal_winner = models.ForeignKey('CountryInfo.Country', blank=True, null=True, related_name='silver_medal_winner+')
    bronze_medal_winner = models.ForeignKey('CountryInfo.Country', blank=True, null=True, related_name='bronze_medal_winner+')
    user = models.ForeignKey('auth.User')