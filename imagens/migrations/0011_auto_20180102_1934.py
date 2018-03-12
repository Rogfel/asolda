# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-02 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imagens', '0010_image_phase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagens.Image'),
        ),
    ]
