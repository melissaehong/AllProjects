# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-31 21:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelbud', '0008_auto_20170831_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='end_date1',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='start_date1',
            new_name='start_date',
        ),
    ]