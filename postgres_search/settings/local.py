# 2014.04.03 18:12:16 EDT
"""
Created on Apr 1, 2014

@author: syerram
"""
from postgres_search.settings.base import *
import logging.config

DATABASES = {
             'default':
             {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'courses',
                'USER': get_env_setting('DB_USER'),
                'PASSWORD': get_env_setting('DB_PASSWORD'),
                'HOST': '',
                'PORT': '5432',
                'SCHEMA': get_env_setting('DB_SCHEMA')
            }
}

SOUTH_DATABASE_ADAPTERS = {
            'default': 'south.db.postgresql_psycopg2'
}

CELERYD_CONCURRENCY = 1
BROKER_URL = 'django://'

logging.config.fileConfig(os.path.join(BASE_DIR, 'logging/local.conf'))
