# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-11 18:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagens', '0013_auto_20180103_0136'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
