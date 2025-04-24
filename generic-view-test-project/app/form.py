from django.db import models

class Car(models.Model):
    name=models.CharField(max_length=100)
    minimum_price=models.IntegerField()
    maximum_price=models.IntegerField()
    cuntry=models.CharField(max_length=100)
    