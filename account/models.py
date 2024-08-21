from django.db import models
from django.contrib.auth.models import User
import random
import string

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    mqtttoken = models.CharField(max_length=7, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.mqtttoken:
            self.mqtttoken = self.generate_unique_mqtttoken()
        super().save(*args, **kwargs)

    def generate_unique_mqtttoken(self):
        while True:
            token = ''.join(random.choices(string.ascii_uppercase, k=7))
            if not Profile.objects.filter(mqtttoken=token).exists():
                return token
            
    def __str__(self):
        return f'{self.user.username}\'s Profile'