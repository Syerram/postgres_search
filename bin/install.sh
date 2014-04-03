#!/bin/bash

if [ ! -f manage.py ]; then
	echo "Please run the script from the root folder"
	exit 1
fi


pip install -r requirements/local.lst
bin/run.sh syncdb --noinput
bin/run.sh migrate --all
bin/run.sh upload_searchable_data $1