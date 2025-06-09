import os
import sys
import json
from datetime import datetime
from app.database import SessionLocal, engine
from app.models import Base, SnippetModel

# Ensure the project root is in sys.path for imports like 'from app...'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


def get_project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


project_root = get_project_root()
DATA_DIR = os.path.join(project_root, "app", "data")

# Create tables if they don't exist yet
Base.metadata.create_all(bind=engine)

db = SessionLocal()
processed, updated, created, skipped = 0, 0, 0, 0

for filename in os.listdir(DATA_DIR):
    if filename.endswith(".json") and not filename.startswith("_"):
        filepath = os.path.join(DATA_DIR, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                snip = json.load(f)
                # Use title as unique key; use something else if more robust
                snippet = db.query(SnippetModel).filter_by(title=snip["title"]).first()
                if snippet:
                    # Update fields if changed
                    changed = False
                    for field in ["code", "explanation", "category", "difficulty"]:
                        new_value = snip.get(field)
                        if getattr(snippet, field) != new_value:
                            setattr(snippet, field, new_value)
                            changed = True
                    if changed:
                        snippet.updated_at = datetime.now()  # assuming model has updated_at
                        db.add(snippet)
                        updated += 1
                        print(f"Updated: {snip['title']}")
                    else:
                        skipped += 1
                        print(f"Unchanged: {snip['title']}")
                else:
                    snippet = SnippetModel(
                        title=snip["title"],
                        code=snip["code"],
                        explanation=snip["explanation"],
                        category=snip.get("category"),
                        difficulty=snip.get("difficulty"),
                        created_at=datetime.now(),
                        updated_at=datetime.now(),  # if your model has this field
                    )
                    db.add(snippet)
                    created += 1
                    print(f"Added: {snip['title']}")
                processed += 1
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

db.commit()
db.close()

print(f"✅ Migration done. {processed} processed, {created} added, {updated} updated, {skipped} unchanged.")
