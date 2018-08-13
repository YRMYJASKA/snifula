from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .import models


class AccountForm(UserChangeForm):
    """Custom Form to modify accounts"""

    class Meta:
        model = models.Account
        fields = ('username', 'email', 'is_banned',)


class RegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = models.Account
        fields = ('username', 'email', )
        help_texts = {
            'username': 'max. 64 characters. (a-Z1-9_+-.)',
            'password2': None,
        }
