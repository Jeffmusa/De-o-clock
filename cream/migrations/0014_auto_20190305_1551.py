# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-05 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cream', '0013_auto_20190305_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='Type',
            field=models.ManyToManyField(related_name='cake_type', to='cream.Type'),
        ),
    ]
