#!/bin/bash

rm -rf neighborlyapi/migrations
rm db.sqlite3
python manage.py makemigrations neighborlyapi
python manage.py migrate

