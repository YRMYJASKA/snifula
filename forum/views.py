from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
import logging

import json
from . import forms
from . import models


@csrf_protect
def viewPost(request, pk):
    if request.method == 'POST':
        form = forms.UserCommentForm(request.POST)
        if form.is_valid() and not request.user.is_anonymous:
            post = get_object_or_404(models.UserPost, pk=pk)
            comment = models.UserComment(
                post=post, author=request.user, content=form.cleaned_data['content'])
            comment.save()
    post = get_object_or_404(models.UserPost, pk=pk)
    form_comment = forms.UserCommentForm
    return render(request, "forum/view.html", {"post": post, "commentform": form_comment})


@method_decorator(login_required, name='dispatch')
class createPost(generic.CreateView):
    model = models.UserPost
    form_class = forms.AddUserPostForm
    template_name = 'forum/create.html'
    success_url = reverse_lazy('postindex')

    def form_valid(self, form):
        newpost = form.save(commit=False)
        newpost.author = self.request.user
        newpost.save()
        return HttpResponseRedirect("/forum/" + str(newpost.id))


def viewIndex(request):
    keyword = request.GET.get('search', '')
    info = ''
    if keyword != '':
        info = "Seach results for: " + keyword
    posts = models.UserPost.objects.filter(
        title__contains=keyword).order_by('-date_published')
    return render(request, 'forum/index.html', {'posts': posts, 'searchinfo': info})
