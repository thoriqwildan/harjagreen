from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
from django.conf import settings

def UserDirectoryPath(instance, filename):
    if not instance.user.id:
        instance.user.save()

    profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_pic_name

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    # profile_pic = models.ImageField(upload_to=UserDirectoryPath, null=True, blank=True, default='default_profile_pic.jpg')

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if self.profile_pic:
    #         img = Image.open(self.profile_pic.path)
    #         if img.height > 300 or img.width > 300:
    #             output_size = (300, 300)
    #             img.thumbnail(output_size, Image.LANCZOS)
    #             img.save(self.profile_pic.path)

    def __str__(self):
        return f'{self.user.username}\'s Profile'