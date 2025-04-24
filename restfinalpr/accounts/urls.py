from django.urls import path
from .views import RegisterView, Logout
from .views import login

urlpatterns = [
    path('login/', login),
    path('register/', RegisterView.as_view(), name='register'),  
    path('logout/', Logout.as_view(), name='logout'),
]
