from django.urls import path

from .views import get_product, create_product

urlpatterns = [
    path('products/<int:product_id>/', get_product),
    path('products/', create_product),
]
