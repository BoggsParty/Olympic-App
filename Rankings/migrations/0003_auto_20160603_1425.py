# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-03 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rankings', '0002_auto_20160603_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranking',
            name='user',
            field=models.CharField(default='', max_length=200),
        ),
    ]
