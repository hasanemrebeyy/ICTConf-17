# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 23:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('speaker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('content', models.TextField(max_length=300)),
                ('hall', models.CharField(default='Konferans Salonu', max_length=40)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='speaker.Speaker')),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('title', 'speaker')]),
        ),
    ]
