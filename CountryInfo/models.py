from django.db import models

class Country(models.Model):
    country_full_name = models.CharField(max_length=200, default='')
    country_abbr_name = models.CharField(max_length=3, default='')
    
    def __str__(self):
        return self.country_full_name
        
class Sport(models.Model):
    sport_name = models.CharField(max_length=200, default='')
    sport_slug = models.SlugField(max_length=50, default='')
    order = models.IntegerField(default=100)
    sport_description = models.TextField(default='Sport Description')
    scoring = models.TextField(default='score')
    favorite = models. TextField(default='favorites')
    competition_dates = models.TextField(default='dates')
    INDIVIDUAL = 'IN'
    TEAM = 'TM'
    WINNER_TYPE = (
    (INDIVIDUAL, 'Individual'),
    (TEAM, 'Team'),
    )
    winner_type = models.CharField(max_length=2, choices=WINNER_TYPE, default=TEAM)
    image = models.URLField(max_length=200, blank=True, default='')
    source_link = models.URLField(max_length=200, blank=True, default='')
    source_text = models.CharField(max_length=200, blank=True, default='')
    view_rankings = models.CharField(max_length=200, blank=True, default='')
    rankings_link = models.URLField(max_length=200, blank=True, default='')
    gold = models.CharField(max_length=200, blank=True, default='TBD')
    silver = models.CharField(max_length=200, blank=True, default='TBD')
    bronze = models.CharField(max_length=200, blank=True, default='TBD')
    def __str__(self):
        return self.sport_name
        
class Athlete(models.Model):
    athlete_full_name = models.CharField(max_length=200, default='')
    sport = models.ManyToManyField(Sport, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.athlete_full_name
        
        