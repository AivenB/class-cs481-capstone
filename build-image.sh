#!/bin/bash
# This script builds a Docker image for a Django application using Podman.
echo "Building Docker image for Django application..."

# Check if Podman is installed
if ! command -v podman &> /dev/null
then
    echo "Podman could not be found. Please install Podman to proceed."
    exit 1
fi

# Check if Dockerfile exists in the current directory
if [ ! -f Dockerfile ]; then
    echo "Dockerfile not found in the current directory. Please ensure you are in the correct directory."
    exit 1
fi

# Build the Docker image using Podman
podman build -t my-django .