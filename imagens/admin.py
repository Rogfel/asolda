# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from imagens import models

# Register your models here.
admin.site.register(models.Image)
# admin.site.register(models.Phase)
# admin.site.register(models.Mod_image)
admin.site.register(models.Parameter)
# admin.site.register(models.Edge)
admin.site.register(models.Project)
# admin.site.register(models.CustomUser)
