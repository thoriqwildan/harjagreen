from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Tool)
admin.site.register(models.Temperature)
admin.site.register(models.SoilMoisture)