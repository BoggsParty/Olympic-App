# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-07-09 18:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CountryInfo', '0016_auto_20160709_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='locked_day',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='locked_time',
        ),
    ]