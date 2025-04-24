from django.db import models


class Post(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
