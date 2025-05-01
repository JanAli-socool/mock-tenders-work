# utils.py

import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def parse_budget(text):
    match = re.search(r'€([\d.,]+)', text)
    if match:
        value = match.group(1).replace('.', '').replace(',', '.')
        return float(value) * 1_000_000 if 'million' in text.lower() else float(value)
    return None

def extract_date(text):
    match = re.search(r'(\w+\s\d{1,2},\s\d{4}|\d{4}-\d{2}-\d{2}|\w+\s\d{1,2},\s?\d{4})', text)
    return match.group(1) if match else None
