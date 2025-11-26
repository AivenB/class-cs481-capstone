#!/bin/bash
# exit 127    # non-zero exit code set to fail the build

# Navigate to the src directory
# cd src || { echo "Directory not found"; exit 1; }

# # Check if the virtual environment already exists
# if [ -d "venv" ]; then
#     echo "Virtual environment already exists. Skipping setup."
# else
#     echo "Creating a new virtual environment..."
#     python -m venv venv
#     echo "Virtual environment setup complete."
# fi

# Activate the virtual environment 
# (fails as command only activates in the current subshell which exits when script finishes)
# NOTE: Virtual environment activation is not required for the build process (containers will not need this step)
# echo "Activating the virtual environment..."
# source venv/bin/activate
# echo "Virtual environment activated."

# Install the required dependencies from requirements.txt
# echo "Installing dependencies..."
# pip install -r requirements.txt
# echo "Dependencies installed."

# Install the required dependencies from requirements.txt
echo "Installing dependencies..."

if ! pip install -r requirements.txt; then
    echo "pip failed, trying pip3..."
    if pip3 install -r requirements.txt; then
        echo "Dependencies installed using pip3."
    else
        echo "Both pip and pip3 failed to install dependencies."
        exit 1
    fi
else
    echo "Dependencies installed using pip."
fi
