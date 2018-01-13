# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 16:57
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Callback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_name', models.CharField(max_length=20)),
                ('call_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
            options={
                'verbose_name': 'Зворотній виклик',
                'db_table': 'callback',
            },
        ),
    ]