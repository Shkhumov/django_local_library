# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 22:29
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_auto_20171013_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_two',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article2_title', models.CharField(max_length=200)),
                ('article2_content', models.TextField()),
            ],
            options={
                'db_table': 'article2',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_title', models.CharField(max_length=200)),
                ('contact_emeil', models.EmailField(blank=True, max_length=50)),
                ('contact_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_date',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_emeil',
        ),
        migrations.RemoveField(
            model_name='article',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='posts',
            name='article',
            field=models.ManyToManyField(to='home.Article'),
        ),
        migrations.AddField(
            model_name='contact',
            name='article',
            field=models.ManyToManyField(to='home.Article'),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article_two',
            name='article',
            field=models.ManyToManyField(to='home.Article'),
        ),
        migrations.AddField(
            model_name='article_two',
            name='article2_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
