from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gismodels

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
    	FieldPanel('body', classname="full"),
    ]

