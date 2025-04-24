from django.contrib.auth import get_user_model
from django.test import TestCase


class TestCustomUser(TestCase):
    def setUp(self):
        self.custom_user = get_user_model()

    def test_auth_user_model_in_settings(self):
        from django.contrib.auth.models import User
        self.assertFalse(self.custom_user == User, '\nیوزرکاستوم مورد نظر را در فایل settings.py تعریف نکرده‌اید.')