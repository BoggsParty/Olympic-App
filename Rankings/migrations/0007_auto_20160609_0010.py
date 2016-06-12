# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-09 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rankings', '0006_auto_20160603_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ranking',
            old_name='user',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='ranking',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='ranking',
            name='username',
            field=models.CharField(default='', max_length=200),
        ),
    ]
