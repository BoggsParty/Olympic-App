# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-07-02 02:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserSelections', '0025_auto_20160701_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='show_jumpingOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('athlete_name', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='show_jumpingSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_name', models.CharField(default='show-jumping', max_length=200)),
                ('place', models.CharField(default='none', max_length=200)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('bronze', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bronze+', to='UserSelections.show_jumpingOptions')),
                ('gold', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gold+', to='UserSelections.show_jumpingOptions')),
                ('silver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='silver+', to='UserSelections.show_jumpingOptions')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
