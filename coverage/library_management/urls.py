from django.urls import path

from library_management import views

urlpatterns = [
    path('booklist/<int:author_age>/<int:book_age>/', views.booklist, name='booklist')
]
