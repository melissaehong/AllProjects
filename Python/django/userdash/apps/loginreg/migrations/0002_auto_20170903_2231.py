# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-03 22:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='created_at',
            new_name='created_att',
        ),
    ]
