# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-06 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0002_auto_20170906_2201'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to='loginreg.User')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_message', to='dashboard.Message')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_owner', to='loginreg.User')),
            ],
        ),
    ]