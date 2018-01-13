# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20171019_0022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Колонка1'},
        ),
        migrations.AlterModelOptions(
            name='article_two',
            options={'verbose_name': 'Колонка2'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name': 'Популярны стилі в дизайні'},
        ),
        migrations.AlterModelOptions(
            name='reclama',
            options={'verbose_name': 'Реклама'},
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_content',
            field=models.TextField(max_length=200, verbose_name='Жатий контент'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_title',
            field=models.CharField(max_length=20, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='reclama',
            name='reclama_content',
            field=models.TextField(max_length=50, verbose_name='Стаття'),
        ),
        migrations.AlterField(
            model_name='reclama',
            name='reclama_title',
            field=models.CharField(max_length=20, verbose_name='Заголовок'),
        ),
    ]
