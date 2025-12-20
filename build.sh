#!/bin/bash
echo "Retriving git"
git pull

source .venv/bin/activate
killall gunicorn 

echo "Building tables"
exec python manage.py migrate --settings=Portfolio.settings.development

echo "Collecting static"
exec python manage.py collectstatic --settings=Portfolio.settings.development --noinput

echo "Launching app"
exec gunicorn -c config/gunicorn/prod.py