from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.datetime_safe import date

from djangoldp.models import Model


class User(AbstractUser, Model):

    class Meta(AbstractUser.Meta, Model.Meta):
        serializer_fields = ['@id', 'username', 'first_name', 'last_name', 'email']
        anonymous_perms = ['view', 'add']
        authenticated_perms = ['inherit', 'change']
        owner_perms = ['inherit']
