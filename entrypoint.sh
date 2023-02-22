#!/bin/sh

set -e

python pydev/manage.py collectstatic --noinput
python pydev/manage.py makemigrations
python pydev/manage.py migrate

python pydev/manage.py runserver 0.0.0.0:8000