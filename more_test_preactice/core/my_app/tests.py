from django.test import TestCase
from .models import Person
import datetime


class PersonTests(TestCase):
    def setUp(self):
        self.ali = Person.objects.create(
            first_name="ali", last_name="zare",
            birth_date=datetime.date(2000, 11, 3)
        )
        self.zahra = Person.objects.create(
            first_name="zahra", last_name="ahmadi",
            birth_date=datetime.date(1930, 1, 3)
        )

    def test_is_young(self):
        ali = Person.objects.get(first_name="ali")
        zahra = Person.objects.get(first_name="zahra")
        self.assertTrue(ali.is_young())
        self.assertFalse(zahra.is_young())

    def test_is_old(self):
        ali = Person.objects.get(first_name='ali')
        zahra = Person.objects.get(first_name='zahra')
        self.assertFalse(ali.is_old())
        self.assertTrue(zahra.is_old())
