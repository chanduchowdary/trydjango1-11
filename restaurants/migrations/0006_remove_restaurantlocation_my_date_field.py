# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 19:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20170807_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantlocation',
            name='my_date_field',
        ),
    ]
