# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-21 14:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0002_auto_20180921_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='truck',
            old_name='truck_follower',
            new_name='followers',
        ),
    ]
