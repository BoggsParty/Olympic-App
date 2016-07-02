from django.db import models
from django.utils import timezone

class eventingOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class eventingSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='eventing')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(eventingOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(eventingOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(eventingOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class womens_all_around_gymnasticsOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class womens_all_around_gymnasticsSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='womens-all-around-gymnastics')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(womens_all_around_gymnasticsOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(womens_all_around_gymnasticsOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(womens_all_around_gymnasticsOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)

class mens_all_around_gymnasticsOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class mens_all_around_gymnasticsSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='mens-all-around-gymnastics')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(mens_all_around_gymnasticsOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(mens_all_around_gymnasticsOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(mens_all_around_gymnasticsOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class womens_track_4x100_relayOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class womens_track_4x100_relaySelection (models.Model):
    sport_name = models.CharField(max_length=200, default='womens-track-4x100-relay')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(womens_track_4x100_relayOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(womens_track_4x100_relayOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(womens_track_4x100_relayOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class mens_track_4x100_relayOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class mens_track_4x100_relaySelection (models.Model):
    sport_name = models.CharField(max_length=200, default='mens-track-4x100-relay')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(mens_track_4x100_relayOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(mens_track_4x100_relayOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(mens_track_4x100_relayOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class womens_decathalonOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class womens_decathalonSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='womens-decathalon')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(womens_decathalonOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(womens_decathalonOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(womens_decathalonOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class mens_decathalonOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class mens_decathalonSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='mens-decathalon')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(mens_decathalonOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(mens_decathalonOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(mens_decathalonOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class womens_swimming_4x100_medley_relayOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class womens_swimming_4x100_medley_relaySelection (models.Model):
    sport_name = models.CharField(max_length=200, default='womens-swimming-4x100-medley-relay')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(womens_swimming_4x100_medley_relayOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(womens_swimming_4x100_medley_relayOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(womens_swimming_4x100_medley_relayOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class mens_swimming_4x100_medley_relayOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class mens_swimming_4x100_medley_relaySelection (models.Model):
    sport_name = models.CharField(max_length=200, default='mens-swimming-4x100-medley-relay')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(mens_swimming_4x100_medley_relayOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(mens_swimming_4x100_medley_relayOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(mens_swimming_4x100_medley_relayOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class womens_swimming_200m_backstrokeOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class womens_swimming_200m_backstrokeSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='womens-swimming-200m-backstroke')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(womens_swimming_200m_backstrokeOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(womens_swimming_200m_backstrokeOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(womens_swimming_200m_backstrokeOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class mens_swimming_1500m_freestyleOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class mens_swimming_1500m_freestyleSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='mens-swimming-1500m-freestyle')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(mens_swimming_1500m_freestyleOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(mens_swimming_1500m_freestyleOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(mens_swimming_1500m_freestyleOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class mens_golfOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class mens_golfSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='mens-golf')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(mens_golfOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(mens_golfOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(mens_golfOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class womens_basketballOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class womens_basketballSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='womens-basketball')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(womens_basketballOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(womens_basketballOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(womens_basketballOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class womens_soccerOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class womens_soccerSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='womens-soccer')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(womens_soccerOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(womens_soccerOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(womens_soccerOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class mens_soccerOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class mens_soccerSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='mens-soccer')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(mens_soccerOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(mens_soccerOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(mens_soccerOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class womens_beach_volleyballOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class womens_beach_volleyballSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='womens-beach-volleyball')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(womens_beach_volleyballOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(womens_beach_volleyballOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(womens_beach_volleyballOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class mens_waterpoloOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class mens_waterpoloSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='mens-waterpolo')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(mens_waterpoloOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(mens_waterpoloOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(mens_waterpoloOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class womens_bmxOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class womens_bmxSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='womens-bmx')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(womens_bmxOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(womens_bmxOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(womens_bmxOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class mens_bmxOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class mens_bmxSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='mens-bmx')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(mens_bmxOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(mens_bmxOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(mens_bmxOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class mens_handballOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class mens_handballSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='mens-handball')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(mens_handballOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(mens_handballOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(mens_handballOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)
    
class show_jumpingOptions (models.Model):
    athlete_name = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.athlete_name

class show_jumpingSelection (models.Model):
    sport_name = models.CharField(max_length=200, default='show-jumping')
    user = models.ForeignKey('auth.User', blank=True, null=True)
    place = models.CharField(max_length=200, default='none')
    gold = models.ForeignKey(show_jumpingOptions,blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey(show_jumpingOptions,blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey(show_jumpingOptions,blank=True, null=True, related_name = 'bronze+')
    date_created = models.DateTimeField(default=timezone.now)