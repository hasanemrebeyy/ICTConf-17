# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 10:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import sponsorship.models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsorship', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorship',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=sponsorship.models.upload_file),
            preserve_default=False,
        ),
    ]