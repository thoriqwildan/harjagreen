from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tools', views.ToolViewSet, basename='tool')
router.register(r"moistures", views.SoilMoistureViewSet, basename="soilmoisture")

urlpatterns = [
    path('', include(router.urls))
]
