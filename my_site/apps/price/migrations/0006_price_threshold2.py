# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0005_auto_20171019_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='threshold2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
