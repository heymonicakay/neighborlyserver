#!/bin/bash

rm -rf neighborlyapi/migrations
rm db.sqlite3
python manage.py makemigrations neighborlyapi
python manage.py migrate
python manage.py loaddata user
python manage.py loaddata token
python manage.py loaddata neighbor
python manage.py loaddata profileimage
python manage.py loaddata category
python manage.py loaddata condition
python manage.py loaddata descriptionaccuracy
python manage.py loaddata reservationstatus
python manage.py loaddata typeofuser
python manage.py loaddata tag
python manage.py loaddata item
python manage.py loaddata itemtag
python manage.py loaddata reservation
python manage.py loaddata message
python manage.py loaddata itemimage
python manage.py loaddata itemreview

