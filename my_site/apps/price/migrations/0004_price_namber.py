# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0003_remove_price_namber'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='namber',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
