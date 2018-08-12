from django import forms

from . import models


class AddUserPostForm(forms.ModelForm):
    """Form to add new UserPosts"""

    class Meta:
        model = models.UserPost
        fields = ('title', 'content', 'author',)


class UserCommentForm(forms.ModelForm):

    class Meta:
        model = models.UserComment
        fields = ('author', 'content', )
