# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 20:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0006_price_threshold2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Price',
        ),
    ]
