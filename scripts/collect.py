
import os
import sys
import requests
from bs4 import BeautifulSoup

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

urls = [
    
    "https://www.perkins.org/resource/how-braille-works/"
]


for i, url in enumerate(urls):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    text = "\n".join(p.get_text() for p in paragraphs)

    with open(f"data/raw/sample_{i}.txt", "w", encoding="utf-8") as f:
        f.write(text)
