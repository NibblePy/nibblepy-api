import json
import os
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "snippets.json"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SNIPPETS_DIR = os.path.join(BASE_DIR, "data")


def get_snippet_by_topic(topic: str) -> dict | None:
    filepath = os.path.join(SNIPPETS_DIR, f"{topic.lower()}.json")
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return None


def load_all_snippets(snippets_dir=SNIPPETS_DIR):
    snippets = {}
    for filename in os.listdir(snippets_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(snippets_dir, filename)
            with open(filepath, "r") as f:
                snippets[filename[:-5]] = json.load(f)
    return snippets
