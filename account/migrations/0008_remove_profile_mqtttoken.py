# Generated by Django 5.1 on 2024-08-23 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_rename_tokenkey_profile_mqtttoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='mqtttoken',
        ),
    ]
