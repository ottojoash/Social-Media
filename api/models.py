from django.db import models
from django.contrib.auth.models import User

class SocialMediaAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)  # e.g., Instagram, Twitter
    access_token = models.TextField()

class ScheduledPost(models.Model):
    account = models.ForeignKey(SocialMediaAccount, on_delete=models.CASCADE)
    content = models.TextField()
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=20, default='Pending')  # e.g., Pending, Posted
