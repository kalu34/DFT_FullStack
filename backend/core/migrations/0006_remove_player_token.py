# Generated by Django 5.1.1 on 2024-09-08 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_player_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='token',
        ),
    ]
