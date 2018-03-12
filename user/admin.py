# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from user import models

admin.site.register(models.CustomUser)
