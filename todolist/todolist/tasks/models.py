from django.db import models
from datetime import date


class User(models.Model):
    GENDER_CHOICE = [
        ('m', 'Male'),
        ('f', 'Female'),
    ]
    user_name = models.CharField(max_length=70)
    nama = models.CharField(max_length=50)
    last_nama = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(max_length=11) 
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)

    def __str__(self):
        return f"{self.user_name} {self.last_nama}"


class Task(models.Model):
    date = models.DateField()
    task_name = models.CharField(max_length=255)
    task_desc = models.TextField()
    clock = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.task_name
