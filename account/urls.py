from django.urls import re_path
from . import views

urlpatterns = [
    re_path('login', views.login_user, name="login"),
    re_path('signup', views.signup_user, name="signup"),
    re_path('test_token', views.test_token)
]
