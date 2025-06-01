import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "snippets.json"


def get_snippets_by_topic(topic: str):
    """Retrieves JSON object for given topic"""
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return data.get(topic.lower())


def fetch_all_snippets():
    """Retrieves JSON object with all snippets"""
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
