# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-13 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0002_auto_20171113_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotteur',
            name='groupes',
            field=models.ManyToManyField(blank=True, to='spot.Groupe'),
        ),
    ]
