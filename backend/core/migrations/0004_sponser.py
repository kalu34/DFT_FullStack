# Generated by Django 5.1.1 on 2024-09-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_tel_shop_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('src', models.ImageField(upload_to='Sponser')),
            ],
        ),
    ]