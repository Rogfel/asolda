# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-03 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagens', '0012_auto_20180103_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='bool_high',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='bool_width',
            field=models.BooleanField(default=False),
        ),
    ]
