from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product


@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        name=request.data['product']['name']
        price=request.data['product']['price']
        product=Product.objects.create(name=name,price=price)
        product.save()
        return Response({
            "name":name,
            "price":price
        }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_product(request, product_id):
    if request.method == 'GET':
        product=Product.objects.get(id=product_id)
        return Response({
            'name': product.name,
            'pricels': product.price,
        }, status=status.HTTP_200_OK)
