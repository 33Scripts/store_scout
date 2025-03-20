from json import load
from os import path


def load_data():
    """Load product data from the data.json file.

    Returns:
        dict: Data loaded from the JSON file, or None if the file is not found.
    """
    try:
        data_path = path.join("data", "data.json")
        with open(data_path) as f:
            return load(f)
    except FileNotFoundError:
        return None
