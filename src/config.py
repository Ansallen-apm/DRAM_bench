import json
import os

def load_config(filepath):
    """Loads timing configuration from a JSON file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Config file not found: {filepath}")
    with open(filepath, 'r') as f:
        return json.load(f)

def load_mapping(filepath):
    """Loads address mapping from a JSON file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Mapping file not found: {filepath}")
    with open(filepath, 'r') as f:
        data = json.load(f)

    # Normalize mapping to list of lists format: [[msb, lsb]]
    # If user provided [msb, lsb], convert to [[msb, lsb]]
    normalized = {}
    for key, value in data.items():
        if isinstance(value[0], int):
            normalized[key] = [value]
        else:
            normalized[key] = value
    return normalized
