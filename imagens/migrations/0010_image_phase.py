# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagens', '0009_auto_20171030_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='phase',
            field=models.FloatField(default=0),
        ),
    ]
