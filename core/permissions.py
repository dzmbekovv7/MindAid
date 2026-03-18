from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff

class IsAdminOrModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['moderator', 'admin']

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

