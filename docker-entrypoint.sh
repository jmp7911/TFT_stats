#!/bin/bash

# Collect static files
echo "Collect static files"
python3 blog/manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python3 blog/manage.py makemigrations
python3 blog/manage.py migrate

# Start server
echo "Starting server"
python3 blog/manage.py runserver 0.0.0.0:8000 --settings=conf.settings.local