from django.db import models
from account.models import Profile
from django.contrib.auth.models import User
import string
import random

# Create your models here.
class Tool(models.Model):
    user = models.ForeignKey(User, related_name="tools", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="gtw")
    created_at = models.DateTimeField(auto_now_add=True)
    mqtttoken = models.CharField(max_length=7, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.mqtttoken:
            self.mqtttoken = self.generate_unique_mqtttoken()
        super().save(*args, **kwargs)

    def generate_unique_mqtttoken(self):
        while True:
            token = ''.join(random.choices(string.ascii_uppercase, k=7))
            if not Tool.objects.filter(mqtttoken=token).exists():
                return token
            

    def __str__(self):
        return f"{self.id}. {self.user}'s Tool"
    
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