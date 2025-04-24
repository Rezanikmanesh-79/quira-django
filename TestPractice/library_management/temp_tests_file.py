from django.test import TestCase
from .models import Member, Book, Borrowed


class MemberModelTest(TestCase):
    def setUp(self):
        self.member = Member.objects.create(first_name="Ali", last_name="Ahmadi")
        self.book1 = Book.objects.create(title="Django for Beginners", genre="Programming")
        self.book2 = Book.objects.create(title="Python Tricks", genre="Programming")
        self.book3 = Book.objects.create(title="Fictional World", genre="Fiction")
        Borrowed.objects.create(member=self.member, book=self.book1)
        Borrowed.objects.create(member=self.member, book=self.book2)

    def test_borrowed_books_all(self):
        borrowed_books = self.member.borrowed_books()
        self.assertEqual(borrowed_books.count(), 2)  

    def test_borrowed_books_filter_by_genre(self):
        programming_books = self.member.borrowed_books("Programming")
        self.assertEqual(programming_books.count(), 2)
        fiction_books = self.member.borrowed_books("Fiction")
        self.assertEqual(fiction_books.count(), 0)  

    def test_borrowed_books_empty(self):
        another_member = Member.objects.create(first_name="Reza", last_name="Moradi")
        self.assertEqual(another_member.borrowed_books().count(), 0)
