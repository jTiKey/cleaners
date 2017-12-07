# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-23 16:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaner',
            name='quality_score',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
