# Generated by Django 5.1 on 2024-08-23 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0004_alter_tool_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
