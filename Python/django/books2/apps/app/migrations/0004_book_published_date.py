# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-27 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_book_in_print'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(default='2006-10-25'),
        ),
    ]