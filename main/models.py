from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):  
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user") 
    follows = models.ManyToManyField(settings.AUTH_USER_MODEL,  symmetrical=False, related_name='following', blank=True)
    follows_count = models.IntegerField(default=0)
    followed = models.ManyToManyField(settings.AUTH_USER_MODEL,  symmetrical=False, related_name='followed', blank=True)
    followed_count = models.IntegerField(default=0)    
    bio = models.TextField(default="no bio")
    created = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=200, default="0.png")

    def __str__(self):  
        return "%s's profile" % self.user 

