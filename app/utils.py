import json
import os
from pathlib import Path
from app.models import SnippetModel

SNIPPETS_DIR = Path(__file__).parent / "data"

# future enhancements and potentially migration from json files
