#!/bin/sh

# Start Taillwind in the background
# echo "Starting Tailwind"
# exec python /app/src/backend/rrd/manage.py tailwind start &

# Start Django
# echo "Starting Django"
# exec python /app/src/backend/rrd/manage.py runserver

echo "Waiting for PostgreSQL at $DB_HOST:$DB_PORT..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done
echo "PostgreSQL is up!"

echo "Running Django migrations..."
python /app/src/backend/rrd/manage.py makemigrations --noinput
python /app/src/backend/rrd/manage.py migrate --noinput

echo "Starting Gunicorn server..."
exec gunicorn rrd.wsgi:application \
    --bind 0.0.0.0:8100 \
    --workers 3 \
    --timeout 120