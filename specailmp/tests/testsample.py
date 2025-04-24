from django.test import TestCase

from people.models import Person


class MigrationTest(TestCase):

    def test_model_is_correct(self):
        info = {
            "first_name": "Lionel",
            "last_name": "Messi",
            "id_code": "1233214567",
            "born_in": "Tehran",
            "birth_year": "1239",
        }
        try:
            Person.objects.create(**info)
        except Exception:
            self.fail("تغییرات مدل Person را به درستی اعمال نکرده‌اید.")