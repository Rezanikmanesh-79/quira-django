from django.urls import path
from .views import library_list_create, library_detail_update_delete,change_password, user_list,HelloView, Login,Register,AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView,LogOut
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    #path('authors/', AuthorList.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('author/new/', AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author_edit'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    #path('login/',Login.as_view(),name='login'),
    path('loged_out/',LogOut.as_view(),name='loged_out'),
    path('hello/',HelloView.as_view(),name='hello'),
    path('NewLogin',obtain_auth_token,name='RestLogin'),
    path('authors/', user_list, name='author_list'),
    path('change_password/', change_password, name='change_password'),
    path('library/<int:library_id>/', library_detail_update_delete, name='library-detail-update-delete'),
    path('libraries/', library_list_create, name='library_list_create'),
    path('api/token/',TokenObtainPairView.as_view),
     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
