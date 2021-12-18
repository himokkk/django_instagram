from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="postauthor", default=1)
    description = models.CharField(max_length=300)
    liked_by = ArrayField(models.IntegerField(default=0), null=True)
    liked_by_count = models.IntegerField(default=0, null=True)
    path = models.CharField(max_length=300, default='/')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.path) 
    

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="commentauthor", default=1)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post", null=True)  
    text = models.CharField(max_length=300)
    liked_by = ArrayField(models.IntegerField(default=0), null=True)
    liked_by_count = models.IntegerField(default=0, null=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)

    