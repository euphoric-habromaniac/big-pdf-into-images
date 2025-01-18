# help.py

def print_help():
    print("""
    PDF to Image Converter - Help Guide

    Welcome to the PDF to Image Converter. This program allows you to convert PDF files
    into images, with various options for quality, output format, and destination.

    -------------------------------
    How to Use:

    1. Convert PDF to Images
        - Select the 'Convert PDF' option from the main menu.
        - Provide the path to the PDF file you want to convert.
        - Choose the output directory where the images will be saved.
        - Select the image quality (DPI) based on your preference:
            * Best quality (higher DPI, larger file size)
            * Default DPI (balanced quality)
            * Save space (lower DPI, smaller file size)
        - The program will convert the PDF into individual image files, one per page.

    2. Configure Settings
        - Select the 'Configure' option from the main menu.
        - Here you can:
            * Set the default DPI (Dots Per Inch) for image quality.
            * Set the default output image format (PNG, JPEG, etc.).
            * Set the default output directory for saving images.

    3. Exit
        - Select the 'Exit' option to quit the program.

    -------------------------------
    Available Settings:

    - Image Format:
        The default image format for converted images. Options include:
        * PNG
        * JPEG
        * JPG

    - DPI (Dots Per Inch):
        The DPI value controls the quality of the converted images:
        * Higher DPI means better quality but larger file sizes.
        * Lower DPI reduces quality but saves disk space.

    - Output Directory:
        The folder where the images will be saved after conversion. You can configure this location to suit your needs.

    -------------------------------
    Troubleshooting:
    - If you encounter any errors during conversion, please make sure:
        * The PDF file path is correct.
        * The output directory is writable.
        * You have the necessary permissions to access the directories involved.

    - If you need more advanced help or have any specific issues, refer to the documentation or reach out for support.

    Enjoy converting PDFs into images!
    """)

if __name__ == "__main__":
    print_help()
