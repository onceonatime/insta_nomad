from django.contrib.auth import get_user_model
from rest_framework import serializers

from images.serializers import CountImageSerializer

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):

    images = CountImageSerializer(many=True, read_only=True)

    post_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = (
            'profile_image',
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count',
            'images',
        )


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'profile_image',
            'username',
            'name',
        )
