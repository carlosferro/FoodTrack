# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-10-01 16:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trucks', '0003_auto_20180921_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='user',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='trucks', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
