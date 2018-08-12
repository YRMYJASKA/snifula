from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from . import forms
from . import models


class AccountAdmin(UserAdmin):
    form = forms.AccountForm
    model = models.Account

    list_display = ['username', 'email', 'score',
                    'posts', 'comments', 'date_joined', 'is_banned']
    readonly_fields = ['score',
                       'posts', 'comments', 'date_joined', 'first_name', 'last_name', 'last_login']


admin.site.register(models.Account, AccountAdmin)
