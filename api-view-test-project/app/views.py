from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book, Author
from .serializers import BookSerializer

class BookListAPIView(APIView):
    def get(self, request,*args,**kwargs):
        books=Book.objects.all()
        serializer = BookSerializer(books, many=True)

    def post(self, request, *args, **kwargs):
        data=request.data('name')
        name=data.get('author')
        book = Book.objects.create(name=name, author=author) 
        serializer=BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)