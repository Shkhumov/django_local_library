# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 16:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0008_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'Прайс лист(ціна)'},
        ),
    ]
