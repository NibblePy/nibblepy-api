import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "snippets.json")


def get_snippets_by_topic(topic: str):
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return data.get(topic.lower())
