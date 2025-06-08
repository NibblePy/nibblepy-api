import os
import json
from datetime import datetime
from app.database import SessionLocal, engine
from app.models import Base, SnippetModel

# Create tables if they don't exist yet
Base.metadata.create_all(bind=engine)

DATA_DIR = "data"

db = SessionLocal()

# Insert all snippets from all JSON files (ignoring any 'related' field)
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".json") and not filename.startswith("_"):
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            snip = json.load(f)  # Each file contains a single snippet dict

            snippet = SnippetModel(
                title=snip["title"],
                code=snip["code"],
                explanation=snip["explanation"],
                category=snip.get("category"),
                difficulty=snip.get("difficulty"),
                created_at=datetime.now(),
            )
            db.add(snippet)

db.commit()
db.close()

print("✅ Migration completed for all JSON files without related snippets.")
