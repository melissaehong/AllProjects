# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-27 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='my_name',
            field=models.CharField(default='Melissa', max_length=45),
        ),
    ]
