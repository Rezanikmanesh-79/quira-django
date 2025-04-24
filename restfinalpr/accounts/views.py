from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import User
from .serializers import UserSerializer


login = obtain_auth_token



class Logout(APIView):

    permission_classes = (IsAuthenticated, )


    def post(self, request):

        request.user.auth_token.delete()

        return Response(data={'message': f"Bye {request.user.username}!"}, status=status.HTTP_204_NO_CONTENT)



class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)  
        user = self.get_queryset().get(username=request.data.get("username"))
        return Response({"id": user.id, "username": user.username}, status=status.HTTP_201_CREATED)
