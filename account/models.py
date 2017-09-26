# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return '{} - profile'.format(self.user.username)