from django.urls import re_path, path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    re_path('login', views.login_user.as_view(), name="login"),
    re_path('signup', views.SignupUser.as_view(), name="signup"),
    path('profile', views.profile_user.as_view(), name="user-profile")
]
