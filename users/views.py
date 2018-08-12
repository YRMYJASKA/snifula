from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.conf import settings

from . import models, forms


def profileView(request, username):
    user = get_object_or_404(models.Account, username=username)
    context = {'user': user}
    return render(request, "users/profile.html", context)


@login_required
def logoutView(request):
    logout(request)
    redirect(settings.LOGOUT_REDIRECT_URL)


class registerView(generic.CreateView):
    form_class = forms.RegistrationForm 
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'
