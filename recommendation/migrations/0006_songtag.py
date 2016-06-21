# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 05:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0005_auto_20160617_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aggressive', models.FloatField(blank=True, null=True)),
                ('ambitious', models.FloatField(blank=True, null=True)),
                ('angry', models.FloatField(blank=True, null=True)),
                ('anxious', models.FloatField(blank=True, null=True)),
                ('bright', models.FloatField(blank=True, null=True)),
                ('calm', models.FloatField(blank=True, null=True)),
                ('carefree', models.FloatField(blank=True, null=True)),
                ('cheerful', models.FloatField(blank=True, null=True)),
                ('cold', models.FloatField(blank=True, null=True)),
                ('complex', models.FloatField(blank=True, null=True)),
                ('confident', models.FloatField(blank=True, null=True)),
                ('detached', models.FloatField(blank=True, null=True)),
                ('difficult', models.FloatField(blank=True, null=True)),
                ('elegant', models.FloatField(blank=True, null=True)),
                ('fun', models.FloatField(blank=True, null=True)),
                ('gentle', models.FloatField(blank=True, null=True)),
                ('happy', models.FloatField(blank=True, null=True)),
                ('harsh', models.FloatField(blank=True, null=True)),
                ('hopeful', models.FloatField(blank=True, null=True)),
                ('hostile', models.FloatField(blank=True, null=True)),
                ('hungry', models.FloatField(blank=True, null=True)),
                ('innocent', models.FloatField(blank=True, null=True)),
                ('intimate', models.FloatField(blank=True, null=True)),
                ('lazy', models.FloatField(blank=True, null=True)),
                ('lively', models.FloatField(blank=True, null=True)),
                ('messy', models.FloatField(blank=True, null=True)),
                ('party', models.FloatField(blank=True, null=True)),
                ('peaceful', models.FloatField(blank=True, null=True)),
                ('relaxed', models.FloatField(blank=True, null=True)),
                ('reserved', models.FloatField(blank=True, null=True)),
                ('reverent', models.FloatField(blank=True, null=True)),
                ('romantic', models.FloatField(blank=True, null=True)),
                ('sad', models.FloatField(blank=True, null=True)),
                ('sexy', models.FloatField(blank=True, null=True)),
                ('silly', models.FloatField(blank=True, null=True)),
                ('smooth', models.FloatField(blank=True, null=True)),
                ('soft', models.FloatField(blank=True, null=True)),
                ('sweet', models.FloatField(blank=True, null=True)),
                ('tender', models.FloatField(blank=True, null=True)),
                ('tense', models.FloatField(blank=True, null=True)),
                ('thoughtful', models.FloatField(blank=True, null=True)),
                ('warm', models.FloatField(blank=True, null=True)),
                ('weary', models.FloatField(blank=True, null=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendation.Song')),
            ],
        ),
    ]