from django.db import models
from .managers import DiscordOAuth2Manager
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.


class DiscordUser(models.Model):
    objects = DiscordOAuth2Manager()

    id = models.BigIntegerField(primary_key=True)
    discord_tag = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    public_flags = models.IntegerField()
    email = models.CharField(max_length=100)
    flags = models.BigIntegerField()
    locale = models.CharField(max_length=100)
    mfa_enabled = models.BooleanField()
    last_login = models.DateTimeField(null=True)

    def is_authenticated(self, request):
        return True


class Project(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    author = models.CharField(max_length=256)
    author_id = models.CharField(max_length=256)
    author_avatar = models.CharField(max_length=256)
    website_link = models.CharField(null=True, blank=True, max_length=500)
    repository_link = models.CharField(null=True, blank=True, max_length=500)
    post_date = models.DateField(auto_now_add=True)
    project_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project')
