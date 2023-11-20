#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py generate_menu_data
python manage.py create_superuser
gunicorn DjangoMenu.wsgi:application --bind 0.0.0.0:8000

exec "$@"
