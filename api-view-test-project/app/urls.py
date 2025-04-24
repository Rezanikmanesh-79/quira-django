from django.urls import path

from app.views import BookListAPIView

urlpatterns = [
    path("books/", BookListAPIView.as_view(), name='book-list-create'),
]
