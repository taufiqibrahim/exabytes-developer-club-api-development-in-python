from tweet.models import Tweet
from rest_framework import serializers


class TweetSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Tweet
        fields = ['url', 'user', 'tweet_text', 'timestamp', ]
