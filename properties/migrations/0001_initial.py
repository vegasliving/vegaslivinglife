# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-03 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dynamic_scraper', '0018_auto_20170503_0408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('thumbnail', models.CharField(blank=True, max_length=200)),
                ('latitude', models.CharField(max_length=40)),
                ('longtitude', models.CharField(max_length=40)),
                ('size', models.PositiveIntegerField(blank=True, null=True)),
                ('numberOfBeds', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('numberOfBaths', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('checker_runtime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dynamic_scraper.SchedulerRuntime')),
            ],
        ),
        migrations.CreateModel(
            name='NewsWebsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('scraper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dynamic_scraper.Scraper')),
                ('scraper_runtime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dynamic_scraper.SchedulerRuntime')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='news_website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.NewsWebsite'),
        ),
    ]
