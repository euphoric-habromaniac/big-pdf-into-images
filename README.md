# pdf-to-pics
  
A Python project that converts PDF files into images (one image per page). This project utilizes the `pdf2image` library to extract pages from PDF files and save them as images for easier viewing and manipulation.
  
## Features
- Convert PDF pages into images.
- Save each page as an image file (JPG, PNG, etc.).
- Customizable output resolution and image format.
  
## Installation
  
### Prerequisites
- Python 3.7 or above.
- pip (Python package manager).
  
### Steps to Install
  
You can install the project in two ways:
  
#### Option 1: Install via pip
  
1. Install directly from PyPI using pip:
  
   ```bash
   pip install big-pdf-into-images==0.1
   ```
  
#### Option 2: Clone the Repository
  
1. Clone the repository:
  
   ```bash
   git clone https://github.com/your-username/pdf-to-pics.git
   cd pdf-to-pics
   ```
  
2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```
  
3. Activate the virtual environment:
   
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
  
4. Install required dependencies:
  
   ```bash
   pip install -r requirements.txt
   ```
  
## Usage
  
Once installed, you can use the command `big-pdf-into-images` to convert a PDF file into images.
    
### Options
  
- By default, the images are saved as PNG files with a resolution of 300 DPI. You can adjust these settings in the script.
  
  
## Dependencies
  
This project uses the following libraries:
  
- `pdf2image`: Convert PDF pages to images.
- `tqdm`: Display a progress bar during conversion.
- `click`: Command-line interface handling.
- `colorama`: Console text formatting.
- `pyfiglet`: Generate ASCII art for visual flair.
- `Pillow`: Image manipulation library for saving and processing images.
  
## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.
  
  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
  
## Acknowledgments
- The `pdf2image` library for making PDF-to-image conversion easy.
- The Python community for providing excellent open-source libraries.
