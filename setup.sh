#!/bin/bash

# Navigate to the src directory
cd src || { echo "Directory not found"; exit 1; }

# Check if the virtual environment already exists
if [ -d "venv" ]; then
    echo "Virtual environment already exists. Skipping setup."
else
    echo "Creating a new virtual environment..."
    python -m venv venv
    echo "Virtual environment setup complete."
fi