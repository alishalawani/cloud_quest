# Generated by Django 5.1.1 on 2024-09-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nimbo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='size',
        ),
        migrations.AddField(
            model_name='machine',
            name='size_gb',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
