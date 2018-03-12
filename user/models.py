# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator


class CustomUser(User):
    username_validator = ASCIIUsernameValidator()

    class Meta:
        proxy = True  # If no new field is added.
        # project = models.OneToManyField('Project')
