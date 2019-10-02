from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from quickstart.views import UserViewSet
from tweet.views import TweetViewSet
from rest_framework_simplejwt.views import TokenObtainPairView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tweets', TweetViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/', include(router.urls)),
]
