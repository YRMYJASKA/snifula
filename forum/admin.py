from django.contrib import admin

from . import models
from . import forms


class CommentsInline(admin.TabularInline):
    model = models.UserComment
    extra = 0
    readonly_fields = ('author', 'score', 'content', 'date_published')


class PostAdmin(admin.ModelAdmin):

    add_form = forms.AddUserPostForm
    list_display = ['title', 'id', 'author',
                    'score', 'content', 'date_published']
    readonly_fields = ['title', 'id', 'author',
                       'score', 'content', 'date_published']
    list_filter = ['date_published']
    inlines = [CommentsInline]


admin.site.register(models.UserPost, PostAdmin)
