from setuptools import setup, find_packages

# Reading the README file for the long description
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='big_pdf_into_images',  # Name of the package
    version='0.1',  # Version of the package
    packages=find_packages(include=['big_pdf_into_images', 'big_pdf_into_images.*']),  # Automatically find packages
    install_requires=[  # Required dependencies
        'pdf2image>=1.16.0',  # To convert PDF to images
        'Pillow>=8.2.0',  # To handle image operations
        'tqdm>=4.59.0',  # To show progress bars
        'requests>=2.25.1',  # For potential HTTP-related functionality
        'jsonschema>=3.2.0',  # In case you need to validate or work with JSON schemas
    ],
    entry_points={  # This creates a command-line tool for easy execution
        'console_scripts': [
            'pdf-to-images=big_pdf_into_images.cli:main',  # Replace 'main' with the entry function in cli.py
        ],
    },
    description='A tool to convert PDF files into images, page by page.',
    long_description=long_description,  # Detailed description read from README
    long_description_content_type='text/markdown',  # Type of content for long_description
    author='Pranjal',  # Replace with your actual name
    author_email='contact@pranjalkumar.com',  # Replace with your actual email
    url='https://github.com/euphoric-habromaniac/big_pdf_into_images',  # Your project URL
    classifiers=[  # Classifiers to categorize your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ],
    python_requires='>=3.6',  # Ensure the package works with Python >=3.6
    include_package_data=True,  # Ensure data files like README.md are included
    data_files=[  # If you have other files to include
        ('config', ['config.json']),  # Example: You may want to include a default config
    ],
    zip_safe=False,  # Set to False if your package contains non-pure Python files (like images or compiled extensions)
    # Optional: Add more metadata about your project, like license, keywords, etc.
    license='MIT',  # Or another license type
    keywords='pdf, images, conversion, pdf2image',  # Relevant keywords for search engines
    tests_require=[  # If you have tests, specify dependencies here
        'pytest>=6.2.0',
        'mock>=4.0.3',
    ],
    test_suite='pytest',  # Point to the testing suite
    # Additional optional configurations
    setup_requires=['setuptools>=40.0'],  # Ensure setuptools is up-to-date
    # If using version control (git, svn, etc.)
    use_scm_version=True,  # Enable version control integration for dynamic versioning
    # Optional: Custom installation steps or scripts
    # cmdclass={...}  
)

