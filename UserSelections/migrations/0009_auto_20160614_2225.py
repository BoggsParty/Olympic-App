# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-15 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSelections', '0008_auto_20160614_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userselection',
            old_name='bronze_winner',
            new_name='winner',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='gold_winner',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='silver_winner',
        ),
        migrations.AddField(
            model_name='userselection',
            name='place',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
