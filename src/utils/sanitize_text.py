# src/utils/sanitize_text.py

import re

def sanitize_smart_characters(text: str) -> str:
    """Replaces smart quotes and other unicode punctuation with ASCII equivalents."""
    replacements = {
        # Smart single quotes and apostrophes
        "‘": "'",
        "’": "'",
        # Smart double quotes
        "“": '"',
        "”": '"',
        # Ellipses
        "…": "...",
        # Dashes
        "–": "-",  # en dash
        "—": "-",  # em dash
        # Non-breaking space
        "\u00A0": " ",
    }

    for smart, ascii_char in replacements.items():
        text = text.replace(smart, ascii_char)

    # Optional: normalize excessive spacing
    text = re.sub(r"\s+", " ", text).strip()

    return text
