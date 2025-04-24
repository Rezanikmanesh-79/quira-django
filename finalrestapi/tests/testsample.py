from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from accounts.models import User


class AccountTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'username': 'somebody', 'password': 'some_password'}
        self.user = User.objects.create_user(**self.user_data)

    def test_login(self):
        url = '/accounts/login/'
        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, '\nاستاتوس‌کد معتبر برای کلاس login برابر 200 است.')
        self.assertTrue('token' in response.data, '\nباید از تابع login آماده‌ی جنگو استفاده کنید.')
        key = response.data.get('token')
        token_query_set = Token.objects.select_related('user').filter(key=key)
        self.assertTrue(token_query_set.exists(), '\nیوزر مورد نظر به درستی لاگین نشده‌ است.')
        token = token_query_set.get()
        self.assertEqual(self.user, token.user, '\nیوزری که لاگین شده است برابر با یوزر مورد نظر نیست.')

    def test_register(self):
        url = '/accounts/register/'
        user_data = {
            'username': 'new_user',
            'password': 'strong_pwd',
        }
        response = self.client.post(url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, '\nاستاتوس‌کد معتبر برای کلاس Register برابر 201 است.')
        user = User.objects.filter(username=user_data['username'])
        self.assertTrue(user.exists(), '\nکلاس Register موجود در فایل views.py را به درستی پیاده‌سازی نکرده‌اید.')