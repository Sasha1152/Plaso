# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-29 14:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0008_auto_20180328_2247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moon',
            options={'ordering': ['planet'], 'verbose_name': 'moon', 'verbose_name_plural': 'moons'},
        ),
    ]
