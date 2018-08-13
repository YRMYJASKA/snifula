from django.urls import path

from . import views

urlpatterns = [
    path('', views.viewIndex, name='forumindex'),
    path('create/', views.createPost.as_view(), name='createpost'),
    path('<int:pk>/', views.viewPost, name='viewpost'),
]
