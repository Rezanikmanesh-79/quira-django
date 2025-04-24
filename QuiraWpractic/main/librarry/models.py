from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.title

class Library(models.Model):
    number = models.IntegerField()  

    def __str__(self):
        return f"Library {self.id}: {self.number}"



