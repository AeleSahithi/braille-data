# config.py

# Directory Paths
RAW_DATA_DIR = "data/raw"
CLEAN_DATA_DIR = "data/clean"
STRUCTURED_DATA_DIR = "data/structured"

# Unified dictionary for easy reference across scripts
PATHS = {
    "raw": RAW_DATA_DIR,
    "clean": CLEAN_DATA_DIR,
    "structured_data": STRUCTURED_DATA_DIR  # Used in structure.py
}


SUPPORTED_FORMATS = [".txt", ".jpg", ".jpeg", ".png", ".pdf"]

# OCR Configuration (can be extended)
OCR_CONFIG = {
    "tesseract_lang": "eng"  # or "hin" for Hindi
}
