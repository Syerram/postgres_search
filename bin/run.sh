#!/bin/bash

if [ ! -f manage.py ]; then
	echo "Please run the script from the root folder"
	exit 1
fi

#bash script to run the manager
export DJANGO_SETTINGS_MODULE="postgres_search.settings.local"

#make sure this is indeed a secret on production
export DB_SCHEMA = "courses"
export DB_USER = "courseuser"
export DB_PASSWORD = "test1234"

./manage.py "$@"