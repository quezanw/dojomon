# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-19 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0009_auto_20181019_2257'),
        ('log_reg', '0003_trainers_trainer_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('teams_pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemons_team', to='dashboard.Pokemon')),
                ('teams_trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainers_team', to='log_reg.Trainers')),
            ],
        ),
    ]
