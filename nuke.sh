#!/bin/bash

rm -rf neighborly/migrations
rm db.sqlite3
python manage.py makemigrations neighborlyapi
python manage.py migrate
python manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata category
python manage.py loaddata descriptionaccuracy
python manage.py loaddata itemstatus
python manage.py loaddata messagestatus
python manage.py loaddata privacy
python manage.py loaddata rating
python manage.py loaddata reservationstatus
python manage.py loaddata responsiveness
python manage.py loaddata tag
python manage.py loaddata usertype

