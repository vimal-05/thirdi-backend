import re

def extract_string(text, start_char, end_char):
    """Extracts the substring between two given characters, including those characters, even across multiple lines."""
    match = re.search(f"{re.escape(start_char)}.*?{re.escape(end_char)}", text, re.DOTALL)
    return match.group(0) if match else None  # Returns None if no match
