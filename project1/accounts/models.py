from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    address = models.TextField(blank=True)
    age = models.PositiveSmallIntegerField(blank=True)
    description = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(
    max_length=1,
    choices=[
        ('M', 'Male'),  
        ('m', 'Male (lowercase)'),
        ('F', 'Female'),
        ('f', 'Female (lowercase)')
    ],
    blank=True
)

    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username
