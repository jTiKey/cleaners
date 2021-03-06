# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-23 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cleaners', '0002_auto_20170523_1907'),
        ('customers', '0002_auto_20170523_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('cleaner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaners.Cleaner')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
            ],
        ),
    ]
