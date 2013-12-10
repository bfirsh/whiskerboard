from __future__ import absolute_import
from django.core.exceptions import ImproperlyConfigured

try:
    from .local import *
except ImportError:
    print "local.py not found, trying deploy.py"
    try:
        from .deploy import *
    except ImportError:
        print "deploy.py not found, we will now die. DIE."
        raise ImproperlyConfigured()
