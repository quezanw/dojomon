# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-23 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='desc',
            field=models.CharField(default='desc', max_length=255),
            preserve_default=False,
        ),
    ]
