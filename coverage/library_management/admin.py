from django.contrib import admin

from library_management.models import Author, Book

admin.site.register(Book)
admin.site.register(Author)
