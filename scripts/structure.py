# scripts/structure.py

import os
import sys
import json

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from config import PATHS  # Assuming you need this for something else

# Define input and output paths
input_dir = os.path.join(project_root, "data", "processed")
output_dir = os.path.join(project_root, "samples",  "output")
output_file = os.path.join(output_dir, "structured_data.json")

# Make sure output directory exists
os.makedirs(output_dir, exist_ok=True)

structured_data = []

# Process each file in the input directory
for file in os.listdir(input_dir):
    file_path = os.path.join(input_dir, file)
    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            structured_data.append({
                "id": file,
                "content": text,
                "metadata": {
                    "source": "OCR/Web",
                    "author": None
                }
            })

# Write structured data to output JSON file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(structured_data, f, indent=4)

print(f"Structured data written to {output_file}")
