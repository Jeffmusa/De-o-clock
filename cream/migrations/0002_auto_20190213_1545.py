# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-13 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cream', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
