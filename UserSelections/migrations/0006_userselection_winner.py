# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-15 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSelections', '0005_auto_20160614_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='userselection',
            name='winner',
            field=models.CharField(default='', max_length=200),
        ),
    ]
