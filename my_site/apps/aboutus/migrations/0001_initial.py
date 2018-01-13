# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(blank=True, max_length=50)),
                ('about_test', models.TextField(blank=True, max_length=200)),
                ('about_img', models.ImageField(blank=True, upload_to='home/img')),
            ],
            options={
                'db_table': 'about',
            },
        ),
    ]
