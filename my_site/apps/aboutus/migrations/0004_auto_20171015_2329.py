# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0003_auto_20171015_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_test',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]