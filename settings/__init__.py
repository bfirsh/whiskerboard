from __future__ import absolute_import
from django.core.exceptions import ImproperlyConfigured
import os

from .base import *

try:
    from .local import *
except ImportError:
    raise ImproperlyConfigured('You need to create settings/local.py and set SECRET_KEY. If you deploy with Fabric, it will automatically create this for you.')

