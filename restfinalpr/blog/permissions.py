from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrAdminOrReadonly(BasePermission):       
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user == obj.author or request.user.is_superuser:
            return True
        return False
