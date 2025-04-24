from django.test import TestCase, Client
from accounts.models import *
from charities.models import Benefactor, Charity, Task


class TestAll(TestCase):
    def setUp(self):
        self.client = Client()
        user = {"username": "Saeid",
                "password": "1q*b12$z",
                "phone": "09133333333",
                "address": "Iran-Tehran",
                "gender": "M",
                "age": "21",
                "description": "This is a test.",
                "first_name": "Saeid",
                "last_name": "Saeidi",
                "email": "Saeid12345@gmail.com"}
        self.user = User.objects.create(**user)
        self.user_2 = User.objects.create(**{**user, "username": "Ali"})
        self.user_3 = User.objects.create(**{**user, "username": "Mohammad"})
        self.user_4 = User.objects.create(**{**user, "username": "Sajjad"})
        
        self.charity = Charity.objects.create(user=self.user, name='charity1', reg_number='1234567891')
        self.charity_2 = Charity.objects.create(user=self.user_2, name='charity2', reg_number='1234567892')
        self.charity_3 = Charity.objects.create(user=self.user_3, name='charity3', reg_number='1234567893')
        self.charity_4 = Charity.objects.create(user=self.user_4, name='charity4', reg_number='1234567894')
        
        self.benefactor = Benefactor.objects.create(user=self.user)
        self.benefactor_2 = Benefactor.objects.create(user=self.user_2)
        self.benefactor_3 = Benefactor.objects.create(user=self.user_3)
        self.benefactor_4 = Benefactor.objects.create(user=self.user_4)
        
        Task.objects.create(title='task1', state='A', charity=self.charity)
        Task.objects.create(title='task2', state='A', charity=self.charity)
        Task.objects.create(title='task3', state='P', charity=self.charity_2, assigned_benefactor=self.benefactor)
        Task.objects.create(title='task4', state='A', charity=self.charity_2, assigned_benefactor=self.benefactor_2)
        Task.objects.create(title='task5', state='A', charity=self.charity_3)
        Task.objects.create(title='task6', state='A', charity=self.charity_3, assigned_benefactor=self.benefactor_2)
        Task.objects.create(title='task7', state='P', charity=self.charity_3, assigned_benefactor=self.benefactor_4)

    def test_related_tasks_to_charity_manager(self):
        objects = Task.objects.related_tasks_to_charity(user=self.user)
        self.assertEqual(objects.count(), 2, '\nتعداد تسک‌هایی که کاربر مورد نظر به عنوان charity است را به درستی محاسبه نکرده‌اید.')
        objects = Task.objects.related_tasks_to_charity(user=self.user_2)
        self.assertEqual(objects.count(), 2, '\nتعداد تسک‌هایی که کاربر مورد نظر به عنوان charity است را به درستی محاسبه نکرده‌اید.')
        objects = Task.objects.related_tasks_to_charity(user=self.user_3)
        self.assertEqual(objects.count(), 3, '\nتعداد تسک‌هایی که کاربر مورد نظر به عنوان charity است را به درستی محاسبه نکرده‌اید.')
        objects = Task.objects.related_tasks_to_charity(user=self.user_4)
        self.assertEqual(objects.count(), 0, '\nتعداد تسک‌هایی که کاربر مورد نظر به عنوان charity است را به درستی محاسبه نکرده‌اید.')

    def test_related_tasks_to_benefactor(self):
        task = Task.objects.first()
        task.assigned_benefactor = self.benefactor
        task.save()
        objects = Task.objects.related_tasks_to_benefactor(user=self.user)
        self.assertEqual(objects.count(), 2, '\nتعداد تسک‌هایی که کاربر مورد نظر به عنوان benefactor است را به درستی محاسبه نکرده‌اید.')
        objects = Task.objects.related_tasks_to_benefactor(user=self.user_2)
        self.assertEqual(objects.count(), 2, '\nتعداد تسک‌هایی که کاربر مورد نظر به عنوان benefactor است را به درستی محاسبه نکرده‌اید.')
        objects = Task.objects.related_tasks_to_benefactor(user=self.user_3)
        self.assertEqual(objects.count(), 0, '\nتعداد تسک‌هایی که کاربر مورد نظر به عنوان benefactor است را به درستی محاسبه نکرده‌اید.')
        objects = Task.objects.related_tasks_to_benefactor(user=self.user_4)
        self.assertEqual(objects.count(), 1, '\nتعداد تسک‌هایی که کاربر مورد نظر به عنوان benefactor است را به درستی محاسبه نکرده‌اید.')

    def test_all_related_tasks_to_user(self):
        # task = Task.objects.first()
        # task.assigned_benefactor = self.benefactor
        # task.save()
        objects = Task.objects.all_related_tasks_to_user(user=self.user)
        self.assertEqual(objects.count(), 4, '\nتعداد تسک‌هایی که کاربر مورد نظر به هر طریقی به آن‌ها دسترسی دارد را به درستی محاسبه نکرده‌اید.')
        objects = Task.objects.all_related_tasks_to_user(user=self.user_2)
        self.assertEqual(objects.count(), 4, '\nتعداد تسک‌هایی که کاربر مورد نظر به هر طریقی به آن‌ها دسترسی دارد را به درستی محاسبه نکرده‌اید.')
        objects = Task.objects.all_related_tasks_to_user(user=self.user_3)
        self.assertEqual(objects.count(), 4, '\nتعداد تسک‌هایی که کاربر مورد نظر به هر طریقی به آن‌ها دسترسی دارد را به درستی محاسبه نکرده‌اید.')
        objects = Task.objects.all_related_tasks_to_user(user=self.user_4)
        self.assertEqual(objects.count(), 2, '\nتعداد تسک‌هایی که کاربر مورد نظر به هر طریقی به آن‌ها دسترسی دارد را به درستی محاسبه نکرده‌اید.')