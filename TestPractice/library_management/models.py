from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def borrowed_books(self, genre=None):
        borrowed_books = Book.objects.filter(
            borrowed__member=self
        )
        if genre:
            borrowed_books = borrowed_books.filter(genre=genre)

        return borrowed_books

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Borrowed(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.member} borrowed {self.book}'
