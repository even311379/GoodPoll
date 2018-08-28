from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Poll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    explination = models.CharField(max_length=400, blank=True)
    created_at = models.DateField(auto_now_add=True)
    poll_logo = models.FileField(blank=True)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PollItem(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    vote = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class VoteHistory(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    pollitem = models.CharField(max_length=200, null=False)
    voter = models.CharField(max_length=200, null=False)
    vote_time = models.DateField(auto_now_add=True)
