# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-06 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
        migrations.AddField(
            model_name='kirrurl',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kirrurl',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]