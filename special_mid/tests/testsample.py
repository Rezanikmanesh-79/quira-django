from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase


class MiddlewareTest(TestCase):
    class FakeRequest:

        def __init__(self, user, *args, **kwargs):
            self.user = user

    @classmethod
    def setUpTestData(cls):
        username = "my_user"
        cls.client_class().post('/accounts/register/', data={
            'username': username,
            'password': 'rereqw1212'
        })
        cls.user = User.objects.get(username=username)

    def setUp(self) -> None:
        self.fake_request = self.FakeRequest(self.user)
        custom_middlewares = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]
        self.new_middlewares = list(
            filter(lambda mw: mw not in custom_middlewares, settings.MIDDLEWARE))

    def test_is_registered(self):
        self.assertGreater(len(self.new_middlewares), 0, msg='\nمیدلور مورد نظر را به درستی به فایل settings.py اضافه نکرده‌اید.')