# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-31 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelbud', '0004_auto_20170831_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
