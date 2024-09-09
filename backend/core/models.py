from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db import models

# Create your models here.
class Player(models.Model):

    AGE_CHOICES = [
        ('U13', 'Under 13'),
        ('U15', 'Under 15'),
        ('U17', 'Under 17'),
    ]

    POSITION_CHOICES=[('GK', 'GK'), ('CB', 'CB'), ('LB', 'LB'), ('RB', 'RB'),('DM', 'DM'), ('CM', 'CM'), ('AM', 'AM'), ('LW', 'LW'),('ST', 'ST'), ('RW', 'RW')]

    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dateOfBirth = models.DateField()
    slug = models.SlugField(max_length=400, unique=True)
    age = models.CharField(max_length=10, choices=AGE_CHOICES)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    position = models.CharField(max_length=20, choices=[('Goalkeeper', 'Goalkeeper'), ('Defender', 'Defender'), ('Midfielder', 'Midfielder'), ('Forward', 'Forward')])
    joinclub = models.TextField()
    foreign = models.CharField(max_length=100, default="No Foreign Club Is Provided")
    localclub = models.CharField(max_length=100, blank=True, null=True)
    academy = models.CharField(max_length=3, null=True)
    oldClub = models.CharField(max_length=100, blank=True, null=True)
    secondaryPosition  = models.CharField(max_length=2, choices=POSITION_CHOICES)
    thirdPosition  = models.CharField(max_length=2, choices=POSITION_CHOICES)
    number = models.IntegerField(default=1)
    preferredFoot =  models.CharField(max_length=30, choices=[('Left','Left'),('Right','Right')])
    phone = models.CharField(max_length=15)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    nationality = models.CharField(max_length=50)
    bio = models.TextField()
    date = models.DateField(auto_now_add=True)
    topPlayer = models.BooleanField(default=False)
    src = models.ImageField(upload_to="Player/", default='default_image.jpg')
    image_2 = models.ImageField(upload_to="Player/" ,default='default_image.jpg')
    link = models.CharField(max_length=300, default="http")

    def __str__(self):
        return self.name

class FormerPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null =True, blank=True)
    position = models.CharField(max_length=20, choices=[('Goalkeeper', 'Goalkeeper'), ('Defender', 'Defender'), ('Midfielder', 'Midfielder'), ('Forward', 'Forward')])
    src = models.ImageField(upload_to="FormerPlayer")
    article = models.TextField(null=True, blank=True)
    startYear = models.DateField()
    endYear = models.DateField()

    def __str__(self):
        return self.player.name
    

class Gallery(models.Model):
    src = models.ImageField(upload_to="Gallery")
    title = models.CharField(max_length=20)
    description = models.TextField()


    def __str__(self):
        return self.title
    
class Staff(models.Model):
    name = models.CharField(max_length=20)
    src = models.ImageField(upload_to="Staff")
    position = models.CharField(max_length=20)
    qualification = models.TextField()
    career = models.TextField()
    facebookLink = models.CharField(max_length=50)
    instagramLink = models.CharField(max_length=50)
    nationality = models.CharField(max_length=100)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Sponser(models.Model):
    name = models.CharField(max_length=100)
    src = models.ImageField(upload_to="Sponser")

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    src = models.ImageField(upload_to="Shop")
    href = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    

class News(models.Model):
    title = models.CharField(max_length=100)
    src = models.ImageField(upload_to="News")
    description = models.TextField()

    def __str__(self):
        return self.title

    


