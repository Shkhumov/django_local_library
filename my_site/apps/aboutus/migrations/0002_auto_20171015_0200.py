# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_img',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_title',
            field=models.CharField(blank=True, default='      ', max_length=50),
        ),
    ]
