#!/bin/bash

rm -rf neighborly/migrations
rm db.sqlite3
python manage.py makemigrations neighborlyapi
python manage.py migrate
python manage.py loaddata users
python manage.py loaddata tokens

