# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField

# Create your models here.
# from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from user.models import CustomUser

# class CustomUser(User):
#     username_validator = ASCIIUsernameValidator()

#     class Meta:
#         proxy = True  # If no new field is added.
#         # project = models.OneToManyField('Project')


# '''
#    clase que define los proyectos para el procesamiento de las
#    imagenes de la solda
# '''


class Project(models.Model):
    date_ini = models.DateField(auto_now_add=True)
    date_end = models.DateField(null=True)
    num_phase = models.PositiveSmallIntegerField(default=1)

    # lider = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique_with='date_ini')
    description = models.TextField(null=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # images = models.OneToManyField('Image')
    # phases = models.OneToManyField('Phase')


class Image(models.Model):
    date_upload = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique_with='date_upload')
    img = models.ImageField(upload_to='images/')
    phase = models.FloatField(default=0)
    # coord_right = models.FloatField(default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    img_diseno = models.CharField(max_length=200, null=True)
    img_bordes = models.CharField(max_length=200, null=True)
    img_values = models.CharField(max_length=200, null=True)

    bool_depth = models.BooleanField(default=False)
    bool_high = models.BooleanField(default=False)
    bool_width = models.BooleanField(default=False)


class Parameter(models.Model):
    variable = models.CharField(max_length=200)
    type_variable = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
