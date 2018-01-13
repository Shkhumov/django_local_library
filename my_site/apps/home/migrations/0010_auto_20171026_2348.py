# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20171022_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_content',
            field=models.TextField(max_length=512, verbose_name='Жатий контент'),
        ),
        migrations.AlterField(
            model_name='reclama',
            name='reclama_content',
            field=models.TextField(max_length=200, verbose_name='Стаття'),
        ),
        migrations.AlterField(
            model_name='reclama',
            name='reclama_title',
            field=models.CharField(max_length=50, verbose_name='Заголовок'),
        ),
    ]
