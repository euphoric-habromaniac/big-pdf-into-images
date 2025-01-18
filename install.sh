#!/bin/bash

# Exit the script on error
set -e

# Ensure the script is run with proper privileges (root for global installs)
if [ "$(id -u)" -ne 0 ]; then
    echo "This script requires superuser privileges. Please run as root or with sudo."
    exit 1
fi

# Print the start message
echo "Starting the installation process..."

# Update package list and install required system dependencies (for example, if you need pip or libraries)
echo "Updating package list..."
sudo apt-get update -y

# Check if pip3 is installed; install it if not
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Installing pip3..."
    sudo apt-get install python3-pip -y
else
    echo "pip3 is already installed."
fi

# Install required Python dependencies from requirements.txt
echo "Installing Python dependencies..."
pip3 install --upgrade pip  # Upgrade pip to the latest version
pip3 install -r requirements.txt

# Handle any installation errors
if [ $? -eq 0 ]; then
    echo "Python dependencies installed successfully."
else
    echo "Error: Failed to install Python dependencies."
    exit 1
fi

# Check if the virtual environment is activated, if not, offer to create one
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Virtual environment not detected. Would you like to create one? (y/n)"
    read -r create_venv
    if [ "$create_venv" == "y" ]; then
        python3 -m venv venv
        source venv/bin/activate
        echo "Virtual environment created and activated."
        echo "Re-running the install process in the virtual environment..."
        pip install -r requirements.txt
    else
        echo "Proceeding without virtual environment."
    fi
else
    echo "Virtual environment detected: $VIRTUAL_ENV"
fi

# Check for config.json and create a default if not present
if [ ! -f config.json ]; then
    echo "config.json not found. Creating a default config..."
    cat <<EOF > config.json
{
    "dpi": 150,
    "format": "png",
    "output_dir": "./images"
}
EOF
    echo "Default config.json created."
else
    echo "config.json found. Skipping creation."
fi

# Test if the script runs successfully by calling the CLI
echo "Testing the package by running the CLI..."
python3 -m big_pdf_into_images.cli --help

if [ $? -eq 0 ]; then
    echo "Installation successful! The package is ready to use."
else
    echo "Error: Failed to run the package CLI."
    exit 1
fi

# Final success message
echo "Installation complete! All dependencies and configurations are set up."