# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20171017_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(blank=True, max_length=200)),
                ('album_text', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'db_table': 'album',
            },
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['title'], 'verbose_name': 'Галерея', 'verbose_name_plural': 'Галерея'},
        ),
        migrations.AddField(
            model_name='album',
            name='connection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Photo'),
        ),
    ]