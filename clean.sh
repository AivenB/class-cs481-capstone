#!/bin/bash
# exit 127

# This script is used to clean the project

# First shutdown the server from container if it is running
echo "Shutting down the server..."
podman-compose down --timeout 5

# Clean the build directory if set