from config import DEFAULT_FORMAT, DEFAULT_DPI, DEFAULT_OUTPUT_DIR
from helpers import validate_pdf_path, create_output_dir, format_file_name, display_progress
from pdf2image import convert_from_path
import os
from tqdm import tqdm

def convert_pdf_to_images(pdf_path, output_dir=None, image_format=None, dpi=None):
    """Converts a PDF file to images (one page at a time) and saves them."""
    # Use defaults if not provided
    image_format = image_format or DEFAULT_FORMAT
    dpi = dpi or DEFAULT_DPI
    output_dir = output_dir or DEFAULT_OUTPUT_DIR
    
    # Validate PDF path
    validate_pdf_path(pdf_path)

    # Ensure output directory exists
    create_output_dir(output_dir)

    # Get the total number of pages in the PDF
    total_pages = len(convert_from_path(pdf_path, dpi=dpi))

    image_paths = []

    # Convert and save each page with progress
    for page_number in tqdm(range(1, total_pages + 1), total=total_pages, desc="Converting PDF", ncols=100):
        image = convert_from_path(pdf_path, first_page=page_number, last_page=page_number, dpi=dpi)[0]

        # Use helper to format the file name
        image_filename = format_file_name(pdf_path, page_number, image_format)
        image_path = os.path.join(output_dir, image_filename)

        # Convert to RGB if JPEG
        if image_format.lower() == 'jpeg':
            image = image.convert('RGB')

        try:
            image.save(image_path, image_format.upper())
        except Exception as e:
            print(f"Error saving image {image_filename}: {e}")
            continue

        image_paths.append(image_path)
        display_progress(page_number, total_pages, task_name="Converting PDF")

    return image_paths



from config import DEFAULT_FORMAT, DEFAULT_DPI, DEFAULT_OUTPUT_DIR
from helpers import validate_pdf_path, create_output_dir
import os

def batch_convert_pdf(pdf_dir, output_base_dir=DEFAULT_OUTPUT_DIR, image_format=DEFAULT_FORMAT, dpi=DEFAULT_DPI):
    """Converts all PDF files in a given directory to images, ignoring non-PDF files."""
    if not os.path.isdir(pdf_dir):
        raise FileNotFoundError(f"Directory not found: {pdf_dir}")

    pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
    non_pdf_files = [f for f in os.listdir(pdf_dir) if not f.endswith('.pdf')]

    if not pdf_files:
        raise ValueError(f"No PDF files found in {pdf_dir}")

    if non_pdf_files:
        print(f"Warning: The following non-PDF files will be ignored: {', '.join(non_pdf_files)}")

    all_image_paths = []
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)
        output_dir = os.path.join(output_base_dir, os.path.splitext(pdf_file)[0])

        image_paths = convert_pdf_to_images(pdf_path, output_dir, image_format, dpi)
        all_image_paths.extend(image_paths)

    return all_image_paths


def get_user_input():
    """Get user input for configuring PDF to image conversion."""
    pdf_file = input("Enter the path to your PDF file: ")
    output_directory = input("Enter the output directory for images: ")
    
    dpi_choice = input("Choose DPI for conversion (300 is high quality, 150 is medium, 72 is low): ")
    try:
        dpi = int(dpi_choice)
    except ValueError:
        print("Invalid DPI value. Using default (300).")
        dpi = 300
    
    image_format = input("Enter the image format (png/jpeg): ").lower()
    if image_format not in ['png', 'jpeg']:
        print("Invalid format. Using 'png' by default.")
        image_format = 'png'

    return pdf_file, output_directory, image_format, dpi


if __name__ == "__main__":
    try:
        pdf_file, output_directory, image_format, dpi = get_user_input()
        images = convert_pdf_to_images(pdf_file, output_directory, image_format, dpi)
        print(f"Conversion complete. Images saved at {output_directory}")
    except Exception as e:
        print(f"Error: {e}")
