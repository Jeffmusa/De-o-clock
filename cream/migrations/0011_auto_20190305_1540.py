# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-05 12:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cream', '0010_auto_20190305_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cake',
            old_name='cake',
            new_name='typ',
        ),
    ]