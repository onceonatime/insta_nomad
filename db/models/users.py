from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from util import Constant


class User(AbstractUser):

    profile_image = models.ImageField(
        null=True,
    )
    name = models.CharField(
        _('Name of User'),
        blank=True,
        max_length=255,
    )
    website = models.URLField(
        null=True,
    )
    bio = models.TextField(
        null=True
    )
    phone = models.CharField(
        max_length=140,
        null=True
    )
    gender = models.CharField(
        max_length=80,
        choices=Constant.GENDER_CHOICES,
        null=True,
    )
    followers = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        related_name='nomadgram_followers',
    )
    following = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        related_name='nomadgram_following',
    )
    push_token = models.TextField(
        default='',
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reversed('users:detail', kwrgs={'username': self.username})

    @property
    def post_count(self):
        return self.images.all().count()

    @property
    def followers_count(self):
        return self.followers.all().count()

    @property
    def following_count(self):
        return self.following.all().count()