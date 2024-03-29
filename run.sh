#!/bin/bash

# Define paths
VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"
MAIN_PY="main.py"

# Create virtual environment if not already created
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    echo "Installing required pip packages..."
    pip install -r "$REQUIREMENTS_FILE"
    echo "Creating export directory..."
    mkdir export
fi

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Run main.py
echo -e "Running main.py..."

# Check if argument is provided
if [ $# -gt 0 ]; then
    python "$MAIN_PY" "$1"
else
    echo -e "\n"
    python "$MAIN_PY"
fi

# Deactivate virtual environment
echo "Deactivating virtual environment..."
deactivate
