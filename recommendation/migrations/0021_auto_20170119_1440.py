# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-19 05:40
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recommendation', '0020_auto_20170115_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situation', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='emotionemotionbasedsong',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 19, 14, 40, 20, 370792)),
        ),
        migrations.AlterField(
            model_name='emotionemotionbasedsong',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 19, 14, 40, 20, 370821)),
        ),
        migrations.AlterField(
            model_name='emotionrelevantsong',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 19, 14, 40, 20, 369988)),
        ),
        migrations.AlterField(
            model_name='emotionrelevantsong',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 19, 14, 40, 20, 370023)),
        ),
        migrations.AlterField(
            model_name='searchsong',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 19, 14, 40, 20, 372827)),
        ),
        migrations.AlterField(
            model_name='searchsong',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 19, 14, 40, 20, 372853)),
        ),
    ]