from tweet.models import Tweet
from tweet.serializers import TweetSerializer
from rest_framework import viewsets
from tweet.permissions import TweetPermission


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [TweetPermission, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)