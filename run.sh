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
fi

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Run main.py
echo -e "Running main.py...\n"
python "$MAIN_PY"

# Deactivate virtual environment
echo "Deactivating virtual environment..."
deactivate
