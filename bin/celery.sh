#!/bin/bash

#see postgres_search/celery.py for more info

export DJANGO_SETTINGS_MODULE="postgres_search.settings.local"
export DB_SCHEMA = "courses"
export DB_USER = "courseuser"
export DB_PASSWORD = "test1234"

celery -A postgres_search worker -l info