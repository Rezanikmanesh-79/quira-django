import json

from django.test import TestCase, Client
from rest_framework import status

from supermarket.models import Product


class ProductTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_product(self):
        Product.objects.create(name='coffee mix', price=3500)

        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK), '\nتابع get_product باید ریسپانسی با استاتوس‌کد 200 بازگرداند.'

        expected = {'name': 'coffee mix', 'price': 3500}
        answer = json.loads(response.content.decode('utf-8'))
        self.assertDictEqual(expected, answer, "\nبرای آبجکتی با نام coffee mix و قیمت 3500، خروجی تابع get_product باید به صورت\n{'name': 'coffee mix', 'price':3500}\nباشد.")