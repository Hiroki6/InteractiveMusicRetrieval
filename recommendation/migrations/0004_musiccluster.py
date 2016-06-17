# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 04:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0003_preference'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendation.Song')),
            ],
        ),
    ]