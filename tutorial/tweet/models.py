from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet_text = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp', ]
