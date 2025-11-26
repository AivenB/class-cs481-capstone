#!/bin/bash
# exit 127    # non-zero exit code set to fail the tests

# cd into Django project directory
cd src/backend/rrd

# Run Django tests
python manage.py test