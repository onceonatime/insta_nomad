from django.conf import settings
from django.db import models
from taggit.managers import TaggableManager

from db.models import TimeStampedModel

__all__ = (
    'Image',
    'Comment',
    'Like',
)


class Image(TimeStampedModel):

    file = models.ImageField()
    location = models.CharField(
        max_length=140,
    )
    caption = models.TextField()
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name='images',
    )
    tags = TaggableManager()

    @property
    def like_count(self):
        return self.likes.all().count()

    @property
    def comment_count(self):
        return self.comments.all().count()

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

    class Meta:
        ordering = ['-created_at']


class Comment(TimeStampedModel):

    message = models.TextField()
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
    )
    image = models.ForeignKey(
        Image,
        null=True,
        related_name='comments',
    )

    def __str__(self):
        return self.message


class Like(TimeStampedModel):

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
    )
    image = models.ForeignKey(
        Image,
        null=True,
        related_name='likes',
    )

    def __str__(self):
        return 'User : {} - Image Caption : {}'.format(self.creator.username, self.image.caption)
