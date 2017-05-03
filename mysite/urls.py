from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from search import views as search_views
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from properties import views as properties_views
from blog import views as blog_views
from home import views as home_views
from VR import views as VR_views
from properties.models import Article

urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^blog-admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^search/$', search_views.search, name='search'),
    url(r'^properties/$', properties_views.article_list, name="properties"),
    url(r'^myhome/$', blog_views.properties_list, name="properties_list"),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^login/$', auth_views.login,name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^GoogleWebVR/', VR_views.GoogleWebVR, name='GoogleWebVR'),
    url(r'^AFrameVR/', VR_views.AFrameVR, name='AFrameVR'),
    url(r'^Unity3DVR/', VR_views.Unity3DVR, name='googleVR'),
    url(r'/stories', include(wagtail_urls)),
    url(r'^$', home_views.home, name="home"),
    url(r'^stories/', home_views.stories, name="stories"),
    url(r'^homes/', home_views.homes, name="homes"),
    url(r'^places/', home_views.places, name="places"),
    url(r'^home-(?P<article_id>[0-9]+)/', home_views.home_detail, name="home_detail")
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
