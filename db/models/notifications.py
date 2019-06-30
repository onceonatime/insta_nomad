from django.conf import settings
from django.db import models

from db.models import Image, TimeStampedModel
from util import Constant


class Notification(TimeStampedModel):

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='creator'
    )
    to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='to'
    )
    notification_type = models.CharField(
        max_length=20,
        choices=Constant.TYPE_CHOICES,
    )
    image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
    )
    comment = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return 'From: {} - To: {}'.format(self.creator, self.to)
