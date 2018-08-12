from django.db import models
from django.conf import settings
from django.utils import timezone

class UserPost(models.Model):
    """User post"""

    # Essential info
    title = models.CharField(max_length=128)
    content = models.TextField()
    score = models.IntegerField(default=0)
    date_published = models.DateTimeField('Date Published', auto_now=True)

    # Author of the post in question
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class UserComment(models.Model):
    """User posted comment on a post"""

    # Add parents for the comment
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Essential info
    content = models.TextField()
    score = models.IntegerField(default=0)
    date_published = models.DateTimeField('Date Published', auto_now=True)
