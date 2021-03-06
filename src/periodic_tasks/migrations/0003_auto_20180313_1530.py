# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-13 13:30
from __future__ import unicode_literals

from django.db import migrations, models

from periodic_tasks.models import tasks_as_choices


class Migration(migrations.Migration):

    dependencies = [
        ('periodic_tasks', '0002_auto_20180223_1228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='periodictask',
            options={'ordering': ('-last_run_dt',)},
        ),
        migrations.AlterField(
            model_name='periodictask',
            name='task',
            field=models.CharField(choices=tasks_as_choices(), max_length=256),
        ),
    ]
