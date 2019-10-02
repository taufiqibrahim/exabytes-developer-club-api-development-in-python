from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_superuser
        elif view.action == 'retrieve':
            return request.user.is_authenticated
        elif view.action == 'create':
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        elif view.action == 'retrieve':
            return obj == request.user or request.user.is_superuser
        else:
            return False
