import json
import os
from pathlib import Path
from app.models import SnippetModel

SNIPPETS_DIR = Path(__file__).parent / "data"


def get_snippet_by_topic(topic: str) -> dict | None:
    filepath = os.path.join(SNIPPETS_DIR, f"{topic.lower()}.json")
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return None


def load_all_snippets():
    snippets = {}
    for file in SNIPPETS_DIR.glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            raw = json.load(f)
            try:
                snippet = SnippetModel(**raw)
                snippet_id = file.stem
                snippets[snippet_id] = snippet
            except Exception as e:
                print(f"❌ Error in {file.name}: {e}")
    return snippets
