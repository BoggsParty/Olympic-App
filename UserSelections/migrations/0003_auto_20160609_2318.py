# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-10 04:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserSelections', '0002_auto_20160607_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userselection',
            name='gold_medal_winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gold_medal_winner+', to='CountryInfo.Country'),
        ),
    ]
