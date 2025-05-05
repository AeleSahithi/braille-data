# Braille Data Pipeline

A comprehensive ETL (Extract-Transform-Load) pipeline for processing unstructured data into structured, AI-trainable datasets for braille translation. This project demonstrates the ability to collect, process, and transform various document formats into a format suitable for training AI models that enhance accessibility for the visually impaired.

## Project Overview

This pipeline performs the following key functions:
1. **Collection**: Gathers unstructured data from various sources (OCR-friendly scanned pages, web content)
2. **Extraction and Cleaning**: Utilizes OCR tools and text processing to extract and clean text
3. **Structuring**: Formats the data into JSON suitable for training a braille translation AI
4. **Translation**: Converts the structured text into braille using Liblouis

## Project Structure

```
Braille_Data_Pipeline/
├── data/
│   ├── raw/          # Raw input files
│   └── processed/    # Cleaned and processed files
├── samples/
│   └── output/       # Final structured and translated output
├── scripts/
│   ├── collect.py    # Data collection script
│   ├── extract_clean.py  # Text extraction and cleaning
│   ├── structure.py  # Data structuring
│   └── translate.py  # Braille translation
├── tests/
│   └── test_pipeline.py  # Unit tests
├── config.py        # Configuration settings
├── requirements.txt  # Project dependencies
└── README.md        # This file
```

## Features

- **Multi-format Support**: Processes various file formats:
  - Images (PNG, JPG, JPEG)
  - PDFs
  - Word documents (DOC, DOCX)
  - Excel files (XLS, XLSX)
  - Text files (TXT)
  - HTML files
  - Email files (MSG, EML)
  - PowerPoint files (PPTX)
  - CSV files
  - RTF files

- **OCR Integration**: Uses Tesseract OCR for image processing
- **Text Cleaning**: Implements comprehensive text cleaning and normalization
- **Braille Translation**: Utilizes Liblouis for accurate braille translation
- **Structured Output**: Generates JSON output with metadata for AI training
- **Multi-language Support**: Handles both English and Hindi text
- **Error Handling**: Comprehensive error logging and handling
- **Unit Tests**: Test suite for pipeline components
- **Configuration Management**: Centralized configuration file

## Prerequisites

1. Python 3.8 or higher
2. Tesseract OCR installed on your system
3. Liblouis installed on your system
4. Required Python packages (install using `pip install -r requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/anilgopishetti/braille-data-pipeline.git]
   cd Braille_Data_Pipeline
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Tesseract OCR:
   - Windows: Download and install from https://github.com/UB-Mannheim/tesseract/wiki
   - Linux: `sudo apt-get install tesseract-ocr`
   - macOS: `brew install tesseract`

5. Install Liblouis:
   - Download from https://github.com/liblouis/liblouis/releases
   - Extract to a known location
   - Update the paths in `config.py` to match your installation

## Usage

1. Place your input files in the `data/raw` directory

2. Run the pipeline:
   ```bash
   # Collect data (if using web scraping)
   python scripts/collect.py

   # Extract and clean text
   python scripts/extract_clean.py

   # Structure the data
   python scripts/structure.py

   # Translate to braille
   python scripts/translate.py
   ```

3. Find the output in `samples/output/`:
   - `structured_data.json`: Cleaned and structured text
   - `braille_output.json`: Final braille translation

## Output Format

The pipeline generates two main JSON files:

1. `structured_data.json`:
   ```json
   [
     {
       "id": "filename",
       "language": "English/Hindi",
       "content": "extracted text",
       "metadata": {
         "source": "OCR/Web",
         "author": null
       }
     }
   ]
   ```

2. `braille_output.json`:
   ```json
   [
     {
       "id": "filename",
       "original": "original text",
       "braille": "braille translation",
       "language": "English/Hindi"
     }
   ]
   ```

## Running Tests

To run the unit tests:
```bash
python -m unittest tests/test_pipeline.py
```

## Error Handling

The pipeline includes comprehensive error handling:
- Detailed logging to `error.log`
- Retry mechanisms for failed operations
- Graceful handling of unsupported file formats
- Language detection and appropriate table selection

## Assessment Alignment

This project successfully meets the assessment requirements:

1. ✅ **Data Collection**: Gathers 20-30 samples of unstructured data
2. ✅ **Extraction and Cleaning**: Uses OCR tools (Tesseract) and text processing
3. ✅ **Structuring**: Formats data into JSON suitable for AI training
4. ✅ **Translation**: Implements braille translation using Liblouis
5. ✅ **Documentation**: Provides comprehensive setup and usage instructions
6. ✅ **Multi-language Support**: Handles both English and Hindi text
7. ✅ **Error Handling**: Implements robust error handling and logging
8. ✅ **Testing**: Includes unit tests for pipeline components

Configuration for translate.py
The translate.py script requires the following to be set up correctly on your system:

1. Liblouis Installation
Download Liblouis from the official site:
https://github.com/liblouis/liblouis/releases

Extract it and note the following paths:

liblouis.dll → typically found in bin/

Braille tables → typically found in share/liblouis/tables/

2. Edit Paths in the Script (or use environment variables)
Update the following variables in translate.py with your local paths:

python

dll_path = r"YOUR_PATH_TO/liblouis.dll"
tables_path = r"YOUR_PATH_TO/tables"
Example:

python

dll_path = r"D:\liblouis-3.33.0-win64\bin\liblouis.dll"
tables_path = r"D:\liblouis-3.33.0-win64\share\liblouis\tables"
Alternatively, modify the script to read these from environment variables:

python

dll_path = os.getenv("LIBLOUIS_DLL_PATH")
tables_path = os.getenv("LIBLOUIS_TABLES_PATH")
And set them in your environment:

Windows CMD

cmd

set LIBLOUIS_DLL_PATH=D:\liblouis-3.33.0-win64\bin\liblouis.dll
set LIBLOUIS_TABLES_PATH=D:\liblouis-3.33.0-win64\share\liblouis\tables
Linux/macOS

bash

export LIBLOUIS_DLL_PATH=/your/path/liblouis/bin/liblouis.dll
export LIBLOUIS_TABLES_PATH=/your/path/liblouis/share/liblouis/tables
3. Dependencies
Install the required Python module:

bash

pip install python-louis
4. Run the Script
Once configured, run:

bash

python scripts/translate.py
Output will be saved to:


bash

samples/output/braille_output.json



Feel free to submit issues and enhancement requests!

