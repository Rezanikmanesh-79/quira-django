from django.urls import path

from app.views import BookListAPIView, BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    # path("books/", BookListAPIView.as_view(), name='book-list-create'),

    path("books/", BookListCreateAPIView.as_view(), name='book-list-create'),
    path("books/<int:pk>/", BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail')
]
