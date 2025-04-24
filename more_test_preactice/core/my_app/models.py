from django.db import models
import datetime


class Person(models.Model):    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def is_young(self):        
        return self.birth_date > datetime.date(1990, 1, 1)

    def is_old(self):
        return self.birth_date < datetime.date(1960, 1, 1)

    def __str__(self):
        return self.first_name
