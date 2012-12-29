from __future__ import absolute_import
from django.core.exceptions import ImproperlyConfigured

try:
    from .deploy import *
except ImportError:
    print "deploy.py not found, trying local.py"
    try:
        from .local import *
    except ImportError:
        print "local.py not found, exiting"
        raise ImproperlyConfigured()
