# Use a lightweight Python base image
FROM python:3.8-slim

# Disable Python stdout buffering
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install OS-level dependencies (Node.js, npm)
# RUN apt-get update && \
#     apt-get install -y nodejs npm build-essential libpq-dev && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*
RUN apt-get update && \
    apt-get install -y nodejs npm netcat-openbsd dos2unix && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy Django project source code
COPY src /app/src/

# Copy requirements and scripts
COPY requirements.txt /app/
COPY *.sh /app/

# Normalize line endings for shell scripts to Unix format (LF not CRLF, important for Windows users)
# RUN find /app -type f -name "*.sh" -exec dos2unix {} \;
RUN dos2unix /app/*.sh 

# Ensure shell scripts are executable
RUN chmod +x /app/*.sh

# Install Python dependencies
RUN /app/build.sh

# Tailwind CSS: install and build for production
RUN python /app/src/backend/rrd/manage.py tailwind install
RUN python /app/src/backend/rrd/manage.py tailwind build

# Collect static files for WhiteNoise
RUN python /app/src/backend/rrd/manage.py collectstatic --noinput

# Expose port for outside container access
EXPOSE 8100

# Set Python path (so Gunicorn can find your Django app)
ENV PYTHONPATH="/app/src/backend/rrd"

# Add a placeholder for SECRET_KEY in case not passed at runtime
# ENV DJANGO_SECRET_KEY="set-this-in-env"

# Start Gunicorn in production
# CMD exec gunicorn rrd.wsgi:application \
#   --bind 0.0.0.0:8100 \
#   --workers 3 \
#   --timeout 120

# Inline entrypoint logic via CMD
CMD /bin/sh -c '\
  echo "Waiting for PostgreSQL at $DB_HOST:$DB_PORT..."; \
  while ! nc -z "$DB_HOST" "$DB_PORT"; do sleep 1; done; \
  echo "PostgreSQL is up!"; \
  echo "Running Django migrations..."; \
  python /app/src/backend/rrd/manage.py makemigrations --noinput; \
  python /app/src/backend/rrd/manage.py migrate --noinput; \
  echo "Starting Gunicorn server..."; \
  exec gunicorn rrd.wsgi:application --bind 0.0.0.0:8100 --workers 3 --timeout 120'

# Start entrypoint script (causes permission issues when using podman-compose up)
# ENTRYPOINT ["/app/entrypoint.sh"]

# define command to run in container to start service
# CMD ["python", "/app/src/backend/rrd/manage.py", "runserver", "0.0.0.0:8100"]
# CMD ["/app/start.sh"] 
# scripts causes error in docker-compose up -d 
# (Error: crun: open exectuable: Permission denied: OCI permission denied)