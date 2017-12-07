# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-23 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
        ('customers', '0003_auto_20170523_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.City'),
        ),
    ]