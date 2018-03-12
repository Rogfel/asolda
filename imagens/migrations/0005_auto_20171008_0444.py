# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-08 04:44
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagens', '0004_auto_20171004_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='static/project_images'),
        ),
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('date_upload',)),
        ),
    ]
