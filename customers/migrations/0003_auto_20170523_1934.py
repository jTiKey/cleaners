# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-23 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20170523_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
