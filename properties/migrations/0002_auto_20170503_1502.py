# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-03 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='numberOfBaths',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='numberOfBeds',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='size',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
