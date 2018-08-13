from django.db import models
from django.conf import settings
from django.utils import timezone

from vote.models import *


class UserPost(VoteModel, models.Model):
    """User post"""

    # Essential info
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_published = models.DateTimeField('Date Published', auto_now=True)

    # Author of the post in question
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.id)


class UserComment(VoteModel, models.Model):
    """User posted comment on a post"""

    # Add parents for the comment
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Essential info
    content = models.TextField()
    date_published = models.DateTimeField('Date Published', auto_now=True)
