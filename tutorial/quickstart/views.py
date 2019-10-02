from django.contrib.auth.models import User
from rest_framework import viewsets
from quickstart.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from quickstart.permissions import UserPermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [UserPermission, ]
