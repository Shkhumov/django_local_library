# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 10:53
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_section',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_status',
        ),
        migrations.AddField(
            model_name='article',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
