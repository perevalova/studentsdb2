# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-09 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20181107_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='teacher_middle_name',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='По батькові'),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='По батькові'),
        ),
    ]
