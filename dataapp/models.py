from django.db import models
from account.models import Profile
from django.contrib.auth.models import User

# Create your models here.
class Tool(models.Model):
    user = models.ForeignKey('auth.User', related_name="tools", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s Tool"
    
class SoilMoisture(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name="soil_moisture")
    moisture_level = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Soil Moisture {self.tool.user}: {self.moisture_level}"
    
class Temperature(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name="temperature")
    temp = models.FloatField()
    humidity = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Temperature {self.tool.user}: {self.temp}"