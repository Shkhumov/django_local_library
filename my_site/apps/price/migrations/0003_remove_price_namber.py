# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 22:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0002_auto_20171019_0106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='namber',
        ),
    ]
