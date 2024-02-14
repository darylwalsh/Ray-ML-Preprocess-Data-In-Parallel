import json
import os

from bs4 import BeautifulSoup


def read_json_file(json_file):
    """Reads a JSON file and returns the list of directories."""
    with open(json_file, 'r') as f:
        directories = json.load(f)
    return directories

def extract_text_from_html(html_content):
    """Extracts and returns text from given HTML content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text(separator=' ', strip=True)

def extract_texts_from_directories(json_file):
    """Navigates directories listed in JSON and extracts text from HTML files."""
    directories = read_json_file(json_file)
    texts = []
    
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        html_content = f.read()
                        text = extract_text_from_html(html_content)
                        texts.append(text)
    
    return texts

# Example usage
json_file = 'directories.json'  # This file should contain a JSON list of directories
texts = extract_texts_from_directories(json_file)
print(texts)
