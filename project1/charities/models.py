from django.db import models
from accounts.models import User


class Benefactor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(blank=True)
    free_time_per_week = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        return f"Benefactor: {self.user.username}"


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    reg_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.CASCADE)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(blank=True)
    age_limit_to = models.IntegerField(blank=True)
    date = models.DateField(blank=True)
    description = models.TextField(blank=True)
    gender_limit = models.CharField(
    max_length=1,
    choices=[
        ('M', 'Male'),
        ('m', 'Male (lowercase)'),
        ('F', 'Female'),
        ('f', 'Female (lowercase)')
    ],
    blank=True
)

    state = models.CharField(max_length=50)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
