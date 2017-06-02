# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-02 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20170602_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='associationFee',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bathsFull',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bathsHalf',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedroomsTotalPossibleNum',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedsTotal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='dryerIncluded',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='listAgentMUI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='matrixUniqueID',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='mlsNumber',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photoCount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='sellingAgentMUI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='sqftTotal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='streetNumber',
            field=models.FloatField(blank=True, null=True),
        ),
    ]