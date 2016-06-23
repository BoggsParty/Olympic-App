# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-23 00:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserSelections', '0021_auto_20160622_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventingselection',
            name='bronze',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bronze+', to='UserSelections.eventingOptions'),
        ),
        migrations.AlterField(
            model_name='eventingselection',
            name='gold',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gold+', to='UserSelections.eventingOptions'),
        ),
        migrations.AlterField(
            model_name='eventingselection',
            name='silver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='silver+', to='UserSelections.eventingOptions'),
        ),
    ]
