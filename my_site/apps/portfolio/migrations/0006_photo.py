# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolio', '0005_delete_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='gallery')),
                ('captions', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name': 'Иллюстрация',
                'verbose_name_plural': 'Иллюстрации',
                'ordering': ['title'],
            },
        ),
    ]