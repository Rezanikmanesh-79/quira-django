from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from .models import Post
from .permissions import IsAuthorOrAdminOrReadonly
from .serializers import PostSerializer


class PostListCreate(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)


post_list_create = PostListCreate.as_view()


class PostRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrAdminOrReadonly,)


post_detail_delete = PostRetrieveDestroy.as_view()
