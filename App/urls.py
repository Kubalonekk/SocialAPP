from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name='register'),
    path('check/', views.check, name='check'),
    path('signout/', views.signout, name="signout"),
    path('login/',
         LoginView.as_view(template_name='App/login.html'),
         name='login'),
    path('add_post/', views.add_post, name="add_post"),
    path('user/<int:pk>/', views.user_profile, name="user_profile"),
    path('add_or_remove_follow/<int:pk>/', views.add_or_remove_follow, name="add_or_remove_follow"),
    path('post/<int:pk>/', views.post, name="post"),
    path('add_or_remove_like/<int:pk>/', views.add_or_remove_like, name="add_or_remove_like"),
    path('friends/', views.friends, name="friends"),
    path('your_profile/', views.your_profile, name="your_profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="App/reset_password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="App/reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="App/reset_password_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="App/reset_password_complete.html"), name="password_reset_complete"),
    
]

