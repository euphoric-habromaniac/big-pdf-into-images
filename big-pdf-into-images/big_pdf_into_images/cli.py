import os
import click
from colorama import Fore, Style, init
import pyfiglet
from big_pdf_into_images.convertor import convert_pdf_to_images, batch_convert_pdf
from big_pdf_into_images.config import DEFAULT_FORMAT, DEFAULT_DPI, DEFAULT_OUTPUT_DIR
from big_pdf_into_images.helpers import load_config, save_config

# Initialize colorama
init(autoreset=True)

# Function to print the banner in ASCII
def print_banner():
    ascii_banner = pyfiglet.figlet_format("PDF2IMAGES")
    print(Fore.CYAN + ascii_banner)

# Main menu handler
def main_menu():
    print_banner()
    print(Fore.GREEN + Style.BRIGHT + "1. Convert PDF")
    print(Fore.GREEN + Style.BRIGHT + "2. Configure how this works")
    print(Fore.GREEN + Style.BRIGHT + "3. Adios (Exit)")

# PDF conversion submenu
def pdf_conversion_menu():
    print(Fore.YELLOW + "\nWhere's the PDF?")
    pdf_path = input(Fore.CYAN + "Enter the path to the PDF: ")
    if not os.path.isfile(pdf_path):
        print(Fore.RED + "PDF not found! Try again.")
        return

    print(Fore.YELLOW + "\nWhere do you want the images to go?")
    output_dir = input(Fore.CYAN + "Enter the output directory: ")
    os.makedirs(output_dir, exist_ok=True)

    print(Fore.YELLOW + "\nHave any wants or needs for the quality?")
    print(Fore.CYAN + "1. Best quality (lots of storage)")
    print(Fore.CYAN + "2. Don't care (default DPI)")
    print(Fore.CYAN + "3. Save space (lower quality)")
    print(Fore.CYAN + "4. Set DPI value yourself")
    print(Fore.CYAN + "5. Go back")

    quality_choice = input(Fore.CYAN + "Choose an option (1-5): ")

    dpi = DEFAULT_DPI
    if quality_choice == '1':
        dpi = 600
    elif quality_choice == '2':
        dpi = 150
    elif quality_choice == '3':
        dpi = 100
    elif quality_choice == '4':
        dpi = int(input(Fore.CYAN + "Enter DPI value: "))
    elif quality_choice == '5':
        return

    print(Fore.GREEN + "\nStarting PDF conversion...")
    try:
        image_paths = convert_pdf_to_images(pdf_path, output_dir, image_format=DEFAULT_FORMAT, dpi=dpi)
        print(Fore.GREEN + f"Conversion complete. Images saved at {output_dir}")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

# Batch PDF conversion submenu
def batch_conversion_menu():
    print(Fore.YELLOW + "\nWhere are the PDFs located?")
    pdf_dir = input(Fore.CYAN + "Enter the directory containing PDFs: ")
    if not os.path.isdir(pdf_dir):
        print(Fore.RED + "Directory not found!")
        return

    print(Fore.YELLOW + "\nWhere do you want to save the images?")
    output_base_dir = input(Fore.CYAN + "Enter the base directory to save images: ")
    os.makedirs(output_base_dir, exist_ok=True)

    print(Fore.YELLOW + "\nChoose the image format (png, jpeg):")
    image_format = input(Fore.CYAN + "Enter the format: ").lower()

    print(Fore.YELLOW + "\nChoose the quality:")
    print(Fore.CYAN + "1. Best quality (lots of storage)")
    print(Fore.CYAN + "2. Don't care (default DPI)")
    print(Fore.CYAN + "3. Save space (lower quality)")
    print(Fore.CYAN + "4. Set DPI value yourself")
    quality_choice = input(Fore.CYAN + "Choose an option (1-4): ")

    dpi = DEFAULT_DPI
    if quality_choice == '1':
        dpi = 600
    elif quality_choice == '2':
        dpi = 150
    elif quality_choice == '3':
        dpi = 100
    elif quality_choice == '4':
        dpi = int(input(Fore.CYAN + "Enter DPI value: "))

    try:
        print(Fore.GREEN + "\nStarting batch conversion...")
        image_paths = batch_convert_pdf(pdf_dir, output_base_dir, image_format=image_format, dpi=dpi)
        print(Fore.GREEN + f"Batch conversion complete. Images saved at {output_base_dir}")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

# Configuration submenu
def config_menu():
    config = load_config()  # Load current configuration
    print(Fore.YELLOW + "\nConfigure your settings:")
    print(Fore.CYAN + "1. Set default DPI")
    print(Fore.CYAN + "2. Set default output format")
    print(Fore.CYAN + "3. Set default output directory")
    print(Fore.CYAN + "4. Go back")

    choice = input(Fore.CYAN + "Choose an option (1-4): ")
    if choice == '1':
        new_dpi = int(input(Fore.CYAN + "Enter the new DPI value: "))
        config['dpi'] = new_dpi
        save_config(config)
        print(Fore.GREEN + f"Default DPI set to {new_dpi}")
    elif choice == '2':
        new_format = input(Fore.CYAN + "Enter the new image format (png, jpeg, jpg): ")
        config['format'] = new_format
        save_config(config)
        print(Fore.GREEN + f"Default format set to {new_format}")
    elif choice == '3':
        new_dir = input(Fore.CYAN + "Enter the new default output directory: ")
        config['output_dir'] = new_dir
        save_config(config)
        print(Fore.GREEN + f"Default output directory set to {new_dir}")
    elif choice == '4':
        return

# Main loop to interact with the user
@click.command()
def cli():
    while True:
        main_menu()
        choice = input(Fore.CYAN + "Choose an option (1-3): ")
        
        if choice == '1':
            pdf_conversion_menu()
        elif choice == '2':
            config_menu()
        elif choice == '3':
            print(Fore.GREEN + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice, please try again.")

if __name__ == "__main__":
    cli()
