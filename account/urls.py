from django.urls import re_path, path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
]
