# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('photo', models.ImageField(upload_to='')),
                ('company', models.CharField(max_length=140)),
                ('github', models.CharField(blank=True, max_length=140)),
                ('linkedin', models.CharField(blank=True, max_length=140)),
                ('twitter', models.CharField(blank=True, max_length=140)),
                ('slug', models.SlugField(editable=False, max_length=60, unique=True)),
            ],
        ),
    ]
