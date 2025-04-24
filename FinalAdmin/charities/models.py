from django.db import models
from accounts.models import User


class Benefactor(models.Model):
    pass


class Charity(models.Model):
    pass


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        pass

    def related_tasks_to_benefactor(self, user):
        pass

    def all_related_tasks_to_user(self, user):
        pass


class Task(models.Model):
    pass
