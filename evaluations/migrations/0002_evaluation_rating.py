# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-27 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='rating',
            field=models.DecimalField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], decimal_places=1, default=3, max_digits=2),
        ),
    ]
