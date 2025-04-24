import datetime

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True)

    def is_alive(self):
        return self.date_of_death is None

    def get_age(self):
        if self.date_of_death is None:
            return datetime.date.today() - self.date_of_birth
        else:
            return self.date_of_death - self.date_of_birth

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField()
    date_of_publish = models.DateField()

    def get_age(self):
        return datetime.date.today() - self.date_of_publish

    def __str__(self):
        return self.title
