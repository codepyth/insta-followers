from django.db import models

# Create your models here.


class FollowersCount(models.Model):
    follower = models.CharField(max_length=30)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user