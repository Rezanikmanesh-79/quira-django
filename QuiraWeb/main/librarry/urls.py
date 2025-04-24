from django.urls import path
from .views import Register, AuthorList, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('author/new/', AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author_edit'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
]
