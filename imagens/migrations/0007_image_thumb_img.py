# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 14:24
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('imagens', '0006_auto_20171009_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumb_img',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='images/'),
        ),
    ]
