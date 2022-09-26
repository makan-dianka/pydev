#!/bin/sh

set -e

python manage.py collectstatic --noinput

uwsgi --socket :5000 --master --enable-threads --module myproject.wsgi