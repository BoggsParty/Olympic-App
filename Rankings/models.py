from django.db import models
from django.utils import timezone

class Ranking(models.Model):
    user = models.ForeignKey('auth.User')
    username = models.CharField(max_length=200, default='')
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=200, default='')
    score = models.IntegerField(default=0)
	       
    #def __str__(self):
        #return self.user
        
class Comments_On(models.Model):
    comments_on = models.BooleanField(default=True)
    
class Comments(models.Model):
    user = models.ForeignKey('auth.User')
    date_created = models.DateTimeField(default=timezone.now)
    comment = models.TextField(max_length=1000)
    
        


