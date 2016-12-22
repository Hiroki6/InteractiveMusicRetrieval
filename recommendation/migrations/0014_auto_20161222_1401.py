# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-22 05:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0013_auto_20161221_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='japanese',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='emotionemotionbasedsong',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 22, 14, 1, 23, 597261)),
        ),
        migrations.AlterField(
            model_name='emotionemotionbasedsong',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 22, 14, 1, 23, 597286)),
        ),
        migrations.AlterField(
            model_name='emotionrelevantsong',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 22, 14, 1, 23, 596440)),
        ),
        migrations.AlterField(
            model_name='emotionrelevantsong',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 22, 14, 1, 23, 596471)),
        ),
        migrations.AlterField(
            model_name='searchsong',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 22, 14, 1, 23, 599127)),
        ),
        migrations.AlterField(
            model_name='searchsong',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 22, 14, 1, 23, 599211)),
        ),
    ]
