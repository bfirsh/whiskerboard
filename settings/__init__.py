from __future__ import absolute_import
from django.core.exceptions import ImproperlyConfigured

try:
    from .local import *
except ImportError:
    print "local.py not found, trying production.py"
    try:
        from .production import *
    except ImportError:
        print "production.py not found, dying."
        raise ImproperlyConfigured()

