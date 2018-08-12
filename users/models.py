from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.utils import timezone


class Account(AbstractUser):
    """Override of Django's default user model"""

    # Some statistics
    posts = models.IntegerField('Num. of posts', default=0)
    comments = models.IntegerField('Num. of comments', default=0)
    score = models.IntegerField('Overall Score', default=0)
    date_joined = models.DateField('Date Joined', default=timezone.now)
    is_banned = models.BooleanField('Banned?', default=False)

    username = models.CharField(
        max_length=64, unique=True, db_index=True, primary_key=True)
    email = models.EmailField()

    def __str__(self):
        return self.username
