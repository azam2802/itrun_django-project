from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    skills = models.CharField(max_length=300)
    birth = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profil_image/')
