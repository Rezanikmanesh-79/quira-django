from django.contrib import admin
from .models import Author, Book

class BookInline(admin.StackedInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country']
    list_filter = ['country']
    list_display_links = ['id', 'name']
    inlines = [BookInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date']
    list_filter = ['author']
    sortable_by = ['published_date']
    list_display_links = ['title', 'author']
