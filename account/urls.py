from django.urls import re_path, path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profile', views.ProfileViewSet, basename='profile')
router.register(r'register', views.RegisterViewSet, basename='register')
router.register(r'login', views.LoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls))    
]
