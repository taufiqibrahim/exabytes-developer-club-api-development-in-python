from rest_framework import permissions

class TweetPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve', ]:
            return True
        if view.action in ['create', 'destroy', ]:
            return request.user.is_authenticated
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'retrieve', ]:
            return True
        elif view.action == 'create':
            return request.user.is_authenticated
        elif view.action == 'destroy':
            return obj.user == request.user
        else:
            return False