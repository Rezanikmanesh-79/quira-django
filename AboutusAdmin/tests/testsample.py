from django.test import TestCase, Client


class AboutUsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_url_works_fine(self):
        response = self.client.get('/about-us/')
        self.assertEqual(200, response.status_code, '\nدرخواست مورد نظر به درستی ارسال نمی‌شود و پاسخ درستی را دریافت نمی‌کند.')
        self.assertContains(response, "نیکوکاران و اعضای خیریه‌ها", msg_prefix='\nصفحه‌ی about_us.html باید شامل عبارت "نیکوکاران و اعضای خیریه‌ها" باشد.')
