from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#!8&23lae2vwb08xar7ho$ys33x7isf%20sv!%z%@)o@^2+n7!'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass


