from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def default_avatar():
    return os.path.join(BASE_DIR, 'truly/static/img/user.svg')


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        upload_to='users/avatars', null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    boi = models.CharField(max_length=500, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    # Social media websites
    facebook = models.URLField(max_length=255, null=True, blank=True)
    instagram = models.URLField(max_length=255, null=True, blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)

    # Settings
    visible = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return '/account/{}/'.format(self.user.username)


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)


class Information(models.Model):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    cover_image = models.URLField(blank=True, null=True)

    email = models.EmailField(max_length=255, blank=True, null=True)
    facebook = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    px500 = models.URLField()

    def __str__(self):
        return self.full_name


class Image(models.Model):
    image_title = models.CharField(max_length=200, blank=False, null=False)
    image_description = models.TextField()
    image_link = models.URLField()
    image_url = models.URLField()

    def __str__(self):
        return self.image_title


class InstagramFeed(models.Model):
    post_title = models.CharField(max_length=200, blank=False, null=False)
    instagram_post_link = models.URLField()

    def __str__(self):
        return self.post_title