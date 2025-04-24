from django.test import TestCase

from accounts.admin import UserAdmin


class UserAdminTest(TestCase):
    def test_credentials_section(self):
        title = UserAdmin.fieldsets[0][0]
        self.assertIsNone(title)
        fields = list(UserAdmin.fieldsets[0][1].get('fields'))
        expected_fields = ['username', 'password']
        self.assertListEqual(fields, expected_fields)
