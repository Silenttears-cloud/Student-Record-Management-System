"""JSON file I/O utilities."""

import json
import os


def load_json(filepath: str) -> dict:
    """Load data from a JSON file. Returns empty dict if not found."""
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return {}


def save_json(filepath: str, data: dict) -> None:
    """Save data to a JSON file with pretty formatting."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
