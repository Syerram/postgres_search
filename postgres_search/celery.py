'''
Created on Apr 3, 2014

@author: syerram
'''
from __future__ import absolute_import
from celery import Celery
from django.conf import settings


app = Celery('postgres_search')
# use string instead of object, so it doesn't have to pickle
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)
