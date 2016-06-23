from django.db import models
from django.utils import timezone

class PasswordReset(models.Model):
    username = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=200, default='')
    date = models.DateTimeField(default=timezone.now)

class LostUserName(models.Model):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=200, default='')
    date = models.DateTimeField(default=timezone.now)
    
class Suggestions(models.Model):
    suggestion = models.TextField(default='')
    user = models.ForeignKey('auth.User', blank=True, null=True)