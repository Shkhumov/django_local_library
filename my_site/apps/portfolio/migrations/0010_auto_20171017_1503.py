# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20171017_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='connection',
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['title'], 'verbose_name': 'Иллюстрация', 'verbose_name_plural': 'Иллюстрации'},
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
