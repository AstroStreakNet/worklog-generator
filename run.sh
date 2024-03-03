#!/bin/bash

# Define paths
VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"
MAIN_PY="main.py"

# Create virtual environment if not already created
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Install required pip packages if not already installed
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing required pip packages..."
    pip install -r "$REQUIREMENTS_FILE"
fi

# Clear terminal before running the script
clear	

# Run main.py
echo "Running main.py..."
python "$MAIN_PY"

# Deactivate virtual environment
echo "Deactivating virtual environment..."
deactivate
