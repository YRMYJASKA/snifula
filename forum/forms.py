from django import forms
from captcha import CaptchaField

from . import models


class AddUserPostForm(forms.ModelForm):
    """Form to add new UserPosts"""
    captcha = CaptchaField()
    class Meta:
        model = models.UserPost
        fields = ('title', 'content')
        labels = {
                'title': 'Title',
                'content': '',
                }


class UserCommentForm(forms.ModelForm):

    captcha = CaptchaField()
    class Meta:
        model = models.UserComment
        fields = ('content', )
        labels = {
            'content': '',
        }
