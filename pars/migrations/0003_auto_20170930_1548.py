# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-30 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pars', '0002_result_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
