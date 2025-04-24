from django.test import TestCase
from .models import Author, Book
import datetime

class LibraryTests(TestCase):
    def setUp(self):
        self.author1 = Author.objects.create(first_name='ali', last_name='alavi', date_of_birth=datetime.date(2000, 1, 1), date_of_death=datetime.date(2010, 1, 1))
        self.author2 = Author.objects.create(first_name='mohammad', last_name='mohammadi', date_of_birth=datetime.date(2000, 1, 1), date_of_death=None)

        self.book1 = Book.objects.create(title='first_book', author=self.author2, summary='this is a summary of first book', date_of_publish=datetime.date(2000, 1, 1))
        self.book2 = Book.objects.create(title='second_book', author=self.author1, summary='this is a summary of second book', date_of_publish=datetime.date(2013, 1, 1))

    def test_is_alive(self):        
        self.assertFalse(self.author1.is_alive())        
        self.assertTrue(self.author2.is_alive())        

    def test_get_age_author(self):
        self.assertEqual(self.author1.get_age(), (self.author1.date_of_death - self.author1.date_of_birth))        
        self.assertEqual(self.author2.get_age(), (datetime.date.today() - self.author1.date_of_birth))        

    def test_str_author(self):
        self.assertEqual(self.author1.__str__(), 'ali alavi')
        self.assertEqual(self.author2.__str__(), 'mohammad mohammadi')
    
    def test_get_age_book(self):
        self.assertEqual(self.book1.get_age(), (datetime.date.today() - self.book1.date_of_publish))  
        self.assertEqual(self.book2.get_age(), (datetime.date.today() - self.book2.date_of_publish))  

    def test_str_book(self):
        self.assertEqual(self.book1.__str__(), 'first_book')
        self.assertEqual(self.book2.__str__(), 'second_book')

    def test_booklist(self):
        response1 = self.client.get('/booklist/1/1/')
        response3 = self.client.get('/booklist/13/15/')
        response2 = self.client.get('/booklist/50/50/')

        self.assertTrue(b"<title>Booklist</title>" in response1.content)
        self.assertEqual(response1.context['good_books'], [])
        self.assertEqual(response1.context['bad_books'], [self.book1, self.book2])

        self.assertTrue(b"<title>Booklist</title>" in response2.content)
        self.assertEqual(response2.context['good_books'], [self.book1, self.book2])
        self.assertEqual(response2.context['bad_books']  , [])


        self.assertTrue(b"<title>Booklist</title>" in response3.content)
        self.assertEqual(response3.context['good_books'], [self.book2])
        self.assertEqual(response3.context['bad_books'], [self.book1])
