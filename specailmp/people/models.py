from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    id_code = models.CharField(max_length=10)
    born_in = models.CharField(max_length=30)
    birth_year = models.PositiveSmallIntegerField()
