# Generated by Django 5.1 on 2024-08-25 05:46

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_remove_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_profile_pic.jpg', null=True, upload_to=account.models.UserDirectoryPath),
        ),
    ]
