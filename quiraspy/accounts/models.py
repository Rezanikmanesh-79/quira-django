from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    national_code = models.CharField(max_length=10, unique=True, verbose_name="National_code")
    height = models.PositiveIntegerField(verbose_name="Hight")
    father_name = models.CharField(max_length=50, verbose_name="Father_name")

    def __str__(self):
        return f"{self.username} - {self.national_code}"
