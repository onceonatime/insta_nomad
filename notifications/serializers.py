from rest_framework import serializers

from db.models import Notification
from images.serializers import SmallImageSerializer
from users.serializers import ListUserSerializer


class NotificationSerializer(serializers.ModelSerializer):

    creator = ListUserSerializer()
    image = SmallImageSerializer()

    class Meta:
        model = Notification
        fields = '__all__'
