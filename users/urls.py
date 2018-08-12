from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',
                                                redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.registerView.as_view(), name='register'),
    path('<slug:username>/', views.profileView, name='profile'),
]
