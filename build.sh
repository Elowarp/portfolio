#!/bin/bash 
set -e #Stops the script at all command that doesn't complete

echo "Retriving git"
git pull

set +e #Allows command to have errors
source .venv/bin/activate
killall gunicorn 

set -e
echo "Building tables"
python manage.py migrate --settings=Portfolio.settings.production --noinput

echo "Collecting static"
python manage.py collectstatic --settings=Portfolio.settings.production --noinput

echo "Launching app"
gunicorn -c config/gunicorn/prod.py