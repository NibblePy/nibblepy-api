import json
from pathlib import Path
import os

# DATA_PATH = os.path.join(os.path.dirname(__file__), "snippets.json")
DATA_PATH = Path(__file__).parent / "data" / "snippets.json"


def get_snippets_by_topic(topic: str):
    """Retrieves JSON object for given topic"""
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return data.get(topic.lower())
