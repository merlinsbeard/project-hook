#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --name hooker \
    --workers 2 \
    --log-level=info \
    --access-logfile -
"$@"
