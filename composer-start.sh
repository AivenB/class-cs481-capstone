#!/bin/bash

# This script is used to start the composer container 
# (must be run from the root directory of the project)
# Check if podman is installed
echo "Checking for Podman and podman-compose..."

if ! command -v podman &> /dev/null; then
    echo "Podman is not installed. Please install Podman to use this script."
    exit 1
fi

# Check if podman-compose is installed
if ! command -v podman-compose &> /dev/null; then
    echo "podman-compose is not installed. Please install podman-compose to use this script."
    exit 1
fi

# Load environment variables (ignoring comments and empty lines)
if [ -f .env ]; then
    set -a
    source <(grep -v '^#' .env | tr -d '\r')
    set +a
fi

# Start the container
echo "Starting containers with HOST_PORT=${HOST_PORT}..."
podman-compose up -d