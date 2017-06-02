# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-30 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_auto_20170505_0247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=300)),
                ('associationFeaturesAvailable', models.CharField(max_length=1000)),
                ('associationFee', models.IntegerField(blank=True, null=True)),
                ('associationFeeMQYN', models.CharField(max_length=200)),
                ('associationFeeIncludes', models.CharField(max_length=1000)),
                ('associationName', models.CharField(max_length=200)),
                ('associationPhoneNumber', models.CharField(max_length=200)),
                ('bathsFull', models.IntegerField(blank=True, null=True)),
                ('bathsHalf', models.IntegerField(blank=True, null=True)),
                ('bathsTotal', models.IntegerField(blank=True, null=True)),
                ('bedroomsTotalPossibleNumber', models.IntegerField(blank=True, null=True)),
                ('bedsTotal', models.IntegerField(blank=True, null=True)),
                ('buildingDescription', models.CharField(max_length=200)),
                ('closePrice', models.IntegerField(blank=True, null=True)),
                ('contructionDescription', models.CharField(max_length=300)),
                ('communityName', models.CharField(max_length=300)),
                ('directions', models.CharField(max_length=2000)),
                ('dryerIncluded', models.IntegerField(blank=True, null=True)),
                ('financingConsidered', models.CharField(max_length=300)),
                ('flooringDescription', models.CharField(max_length=300)),
                ('garageDescription', models.CharField(max_length=500)),
                ('houseFaces', models.CharField(max_length=100)),
                ('lastListPrice', models.IntegerField(blank=True, null=True)),
                ('listAgentMUI', models.IntegerField(blank=True, null=True)),
                ('listAgentFullName', models.CharField(max_length=300)),
                ('listOfficeName', models.CharField(max_length=300)),
                ('listOfficePhone', models.CharField(max_length=200)),
                ('matrixUniqueID', models.IntegerField(blank=True, null=True)),
                ('matrixModifiedDT', models.TimeField()),
                ('mlsNumber', models.IntegerField(blank=True, null=True)),
                ('mls', models.CharField(max_length=100)),
                ('photoCount', models.IntegerField(blank=True, null=True)),
                ('postalCode', models.CharField(max_length=10)),
                ('propertyCondition', models.CharField(max_length=100)),
                ('propertySubType', models.CharField(max_length=100)),
                ('publicAddress', models.CharField(max_length=300)),
                ('publicRemarks', models.CharField(max_length=1000)),
                ('sellingAgentMUI', models.IntegerField(blank=True, null=True)),
                ('sellingAgentFullName', models.CharField(max_length=400)),
                ('sellingAgentDirectWorkPhone', models.CharField(max_length=300)),
                ('streetName', models.CharField(max_length=200)),
                ('streetNumber', models.IntegerField(blank=True, null=True)),
                ('subdivisionName', models.CharField(max_length=200)),
                ('sqftTotal', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]