import os
import shutil

def validate_pdf_path(pdf_path):
    """Checks if the PDF file exists at the given path."""
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    return True

def create_output_dir(output_dir):
    """Creates the output directory if it does not exist."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def clean_output_dir(output_dir):
    """Removes existing files in the output directory to ensure a fresh start."""
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    return output_dir

def get_user_input(prompt, valid_responses=None, default=None):
    """Handles user input with optional validation."""
    while True:
        user_input = input(prompt).strip()
        if not user_input and default is not None:
            return default
        if valid_responses and user_input not in valid_responses:
            print(f"Invalid choice. Valid options are: {valid_responses}")
        else:
            return user_input

def format_file_name(file_path, page_number, file_extension='png'):
    """Generates a formatted file name for the image."""
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    return f"{base_name}_page_{page_number}.{file_extension}"

def display_progress(current, total, task_name="Processing"):
    """Displays a simple progress message in the format: task_name: current/total."""
    progress = (current / total) * 100
    print(f"{task_name}: {current}/{total} ({progress:.2f}%) completed.")

def validate_dpi(dpi):
    """Validates the DPI value entered by the user."""
    if not isinstance(dpi, int) or dpi <= 0:
        raise ValueError("DPI must be a positive integer.")
    return dpi

def get_output_format_choice():
    """Gets the preferred output image format from the user."""
    print("Choose an image format for the conversion:")
    print("1. PNG")
    print("2. JPEG")
    print("3. JPG")
    
    choice = get_user_input("Enter choice (1-3): ", valid_responses=['1', '2', '3'])
    return {'1': 'png', '2': 'jpeg', '3': 'jpg'}[choice]

def handle_conversion_error(e):
    """Handles errors during PDF conversion."""
    print(f"Error during conversion: {e}")
    print("Please make sure the PDF is valid, and try again.")

import json
import os

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {
        'dpi': 150,
        'format': 'png',
        'output_dir': './images'
    }

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
