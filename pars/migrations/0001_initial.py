# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 15:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField(default='', verbose_name='段落内容')),
                ('count', models.IntegerField(default=0, verbose_name='使用统计')),
            ],
            options={
                'verbose_name': '段落信息',
                'verbose_name_plural': '段落信息',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='问题内容')),
                ('answer', models.TextField(verbose_name='答案内容')),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pars.Paragraph', verbose_name='段落')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '段落信息',
                'verbose_name_plural': '段落信息',
            },
        ),
    ]