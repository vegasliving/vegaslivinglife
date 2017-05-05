#Stage 2 Update (Python 3)
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.gis.db import models as gismodels
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from scrapy_djangoitem import DjangoItem
from dynamic_scraper.models import Scraper, SchedulerRuntime


@python_2_unicode_compatible
class NewsWebsite(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=200)
    news_website = models.ForeignKey(NewsWebsite) 
    description = models.TextField(blank=True)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    url = models.URLField(blank=True)
    thumbnail = models.CharField(max_length=200, blank=True)
    latitude = models.CharField(max_length=40)
    longtitude = models.CharField(max_length=40)
    detail_description = models.CharField(max_length=2000, blank=True, null=True)
    size = models.CharField(max_length=200, blank=True, null=True,)
    numberOfBeds = models.CharField(max_length=200, blank=True, null=True,)
    numberOfBaths = models.CharField(max_length=200, blank=True, null=True,)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title


class ArticleItem(DjangoItem):
    django_model = Article


@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
    if isinstance(instance, NewsWebsite):
        if instance.scraper_runtime:
            instance.scraper_runtime.delete()
    
    if isinstance(instance, Article):
        if instance.checker_runtime:
            instance.checker_runtime.delete()
            
pre_delete.connect(pre_delete_handler)