from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

login = obtain_auth_token


class Logout(APIView):
    """
    Delete user's authtoken
    """
    pass


class Register(CreateAPIView):
    """
    Create a new user
    """
    pass
