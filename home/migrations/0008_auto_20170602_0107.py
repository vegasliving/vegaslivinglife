# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-02 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170602_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='closePrice',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
