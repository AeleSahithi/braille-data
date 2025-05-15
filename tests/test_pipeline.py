import unittest
import os
import json
from pathlib import Path
import sys

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.extract_clean import clean_text
from scripts.structure import structure_data
from scripts.translate import translate_to_braille
from config import PATHS, SUPPORTED_FORMATS

class TestBraillePipeline(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        # Create test directories if they don't exist
        os.makedirs(os.path.dirname(PATHS["structured_data"]), exist_ok=True)
        os.makedirs(os.path.dirname(PATHS["braille_output"]), exist_ok=True)

    def test_clean_text(self):
        """Test text cleaning functionality"""
        test_cases = [
            ("Hello\nWorld", "Hello World"),
            ("  Extra  Spaces  ", "Extra Spaces"),
            ("Mixed\nLines\nAnd\nSpaces", "Mixed Lines And Spaces"),
            ("", ""),
            ("नमस्ते\nदुनिया", "नमस्ते दुनिया")  # Hindi text
        ]
        
        for input_text, expected in test_cases:
            with self.subTest(input_text=input_text):
                self.assertEqual(clean_text(input_text), expected)

    def test_structure_data(self):
        """Test data structuring functionality"""
        test_data = [
            {"id": "test1", "content": "Hello World"},
            {"id": "test2", "content": "नमस्ते दुनिया"}
        ]
        
        structure_data(test_data)
        
        # Verify structured data file exists and contains correct format
        self.assertTrue(os.path.exists(PATHS["structured_data"]))
        with open(PATHS["structured_data"], "r", encoding="utf-8") as f:
            structured = json.load(f)
            self.assertEqual(len(structured), len(test_data))
            self.assertIn("language", structured[0])
            self.assertIn("metadata", structured[0])

    def test_translate_to_braille(self):
        """Test braille translation functionality"""
        test_data = [
            {"id": "test1", "content": "Hello"},
            {"id": "test2", "content": "नमस्ते"}
        ]
        
        # First structure the data
        structure_data(test_data)
        
        # Then translate to braille
        translate_to_braille()
        
        # Verify braille output file exists and contains correct format
        self.assertTrue(os.path.exists(PATHS["braille_output"]))
        with open(PATHS["braille_output"], "r", encoding="utf-8") as f:
            braille_data = json.load(f)
            self.assertEqual(len(braille_data), len(test_data))
            self.assertIn("braille", braille_data[0])

    def test_supported_formats(self):
        """Test supported file formats"""
        all_formats = []
        for formats in SUPPORTED_FORMATS.values():
            all_formats.extend(formats)
        
        # Test that all formats are unique
        self.assertEqual(len(all_formats), len(set(all_formats)))
        
        # Test that common formats are supported
        self.assertIn(".txt", all_formats)
        self.assertIn(".pdf", all_formats)
        self.assertIn(".docx", all_formats)


if __name__ == '__main__':
    unittest.main() # minor edit
