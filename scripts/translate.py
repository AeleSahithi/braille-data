import ctypes
import os
import sys
import json

def check_path(path, description):
    """Check if a path exists and print appropriate message."""
    if not os.path.exists(path):
        print(f"Error: {description} not found at {path}")
        return False
    return True

def main():
    # Configuration
    dll_path = r"D:\liblouis-3.33.0-win64\bin\liblouis.dll"
    tables_path = r"D:\liblouis-3.33.0-win64\share\liblouis\tables"
    input_file = "samples/output/structured_data.json"
    output_file = "samples/output/braille_output.json"
    table_file = os.path.join(tables_path, "en-ueb-g2.ctb")

    print("Checking Liblouis installation...")
    if not check_path(dll_path, "Liblouis DLL") or not check_path(table_file, "Unicode braille table"):
        print("Please ensure Liblouis and required tables are installed correctly.")
        return 1

    # Load DLL
    try:
        print("Loading Liblouis DLL...")
        ctypes.cdll.LoadLibrary(dll_path)
    except Exception as e:
        print(f"Error loading DLL: {e}")
        return 1

    # Import louis after DLL is loaded
    try:
        import louis
    except ImportError:
        print("Error: 'python-louis' module is not installed. Install it via 'pip install python-louis'")
        return 1

    # Set tables path
    os.environ['LOUIS_TABLEPATH'] = tables_path

    # Check input file
    if not check_path(input_file, "Input file"):
        return 1

    # ASCII to Unicode Braille mapping
    ASCII_TO_UNICODE_BRAILLE = {
        'a': '\u2801', 'b': '\u2803', 'c': '\u2809', 'd': '\u2819', 'e': '\u2811',
        'f': '\u280b', 'g': '\u281b', 'h': '\u2813', 'i': '\u280a', 'j': '\u281a',
        'k': '\u2805', 'l': '\u2807', 'm': '\u280d', 'n': '\u281d', 'o': '\u2815',
        'p': '\u280f', 'q': '\u281f', 'r': '\u2817', 's': '\u280e', 't': '\u281e',
        'u': '\u2825', 'v': '\u2827', 'w': '\u283a', 'x': '\u282d', 'y': '\u283d',
        'z': '\u2835',
        '1': '\u2801', '2': '\u2803', '3': '\u2809', '4': '\u2819', '5': '\u2811',
        '6': '\u280b', '7': '\u281b', '8': '\u2813', '9': '\u280a', '0': '\u281a',
        ',': '\u2802', ';': '\u2806', ':': '\u2812', '.': '\u2832', '!': '\u2816',
        '(': '\u2826', ')': '\u2826', '?': '\u2822', '-': '\u2824', '/': '\u282c',
        '"': '\u2810', '*': '\u282a', '@': '\u2800', '#': '\u2820', '$': '\u2830',
        '%': '\u2834', '&': '\u2828', '+': '\u2822', '>': '\u2838', '<': '\u2828',
        '=': '\u2836', '_': '\u2838', '~': '\u283c', '^': '\u2820',
    }

    def ascii_to_unicode_braille(ascii_braille):
        return ''.join(ASCII_TO_UNICODE_BRAILLE.get(ch, ch) for ch in ascii_braille)

    try:
        print("Reading input file...")
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        print("Translating content to braille...")
        braille_output = []
        for entry in data:
            try:
                ascii_braille = louis.translate([table_file], entry["content"], typeform=None, mode=0)[0]
                unicode_braille = ascii_to_unicode_braille(ascii_braille)
                braille_output.append({
                    "id": entry["id"],
                    "original": entry["content"],
                    "braille": unicode_braille
                })
            except Exception as e:
                print(f"Error translating entry {entry.get('id', 'unknown')}: {e}")
                continue

        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        print("Writing output file...")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(braille_output, f, indent=4, ensure_ascii=False)

        print("Translation completed successfully!")
        return 0

    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
