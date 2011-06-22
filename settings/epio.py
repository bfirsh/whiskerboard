from __future__ import absolute_import
from .base import *

from bundle_config import config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config['postgres']['database'],
        'USER': config['postgres']['username'],
        'PASSWORD': config['postgres']['password'],
        'HOST': config['postgres']['host'],
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '{host}:{port}'.format(
                host=config['redis']['host'],
                port=config['redis']['port']),
        'OPTIONS': {
            'PASSWORD': config['redis']['password'],
        },
        'VERSION': config['core']['version'],
    },
}

DEBUG = False

