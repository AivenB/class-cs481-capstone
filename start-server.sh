#!/bin/sh

# Exit immediately if a command exits with a non-zero status
# set -e

# echo "Applying database migrations..."  # (migrate) to ensure database is up-to-date
# python /app/src/manage.py migrate --noinput

# echo "Collecting static files..."       # (collectstatic) to ensure static files are collected if needed
# python /app/src/manage.py collectstatic --noinput

echo "Starting Django development server..."
# exec python /app/src/manage.py runserver 0.0.0.0:8000
exec python /app/src/backend/rrd/manage.py runserver 0.0.0.0:8100