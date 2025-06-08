import json
import sys
import os

REQUIRED_FIELDS = {"title", "code", "explanation", "difficulty", "category"}
ALLOWED_DIFFICULTIES = {"beginner", "intermediate", "advanced"}


def get_project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def load_categories(categories_path):
    with open(categories_path, "r", encoding="utf-8") as f:
        return set(json.load(f))


def validate_snippet_file(snippet_path, categories):
    errors = []
    if os.path.basename(snippet_path).startswith("_TEMPLATE"):
        return None

    with open(snippet_path, "r", encoding="utf-8") as f:
        try:
            snippet = json.load(f)
        except json.JSONDecodeError as e:
            return [f"{snippet_path}: JSON decode error: {e}"]

    missing = REQUIRED_FIELDS - set(snippet.keys())
    if missing:
        errors.append(f"{snippet_path}: Missing fields: {', '.join(missing)}")

    difficulty = snippet.get("difficulty")
    if difficulty and difficulty not in ALLOWED_DIFFICULTIES:
        errors.append(f"{snippet_path}: Invalid difficulty '{difficulty}'. Must be one of {ALLOWED_DIFFICULTIES}")

    category = snippet.get("category")
    if category and category not in categories:
        errors.append(f"{snippet_path}: Invalid category '{category}'. Must be one of {sorted(categories)}")

    return errors if errors else None


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate_snippets.py [snippet-file-name or app/data/filename.json]")
        sys.exit(1)

    project_root = get_project_root()
    data_dir = os.path.join(project_root, "app", "data")
    categories_path = os.path.join(data_dir, "_CATEGORIES.json")
    if not os.path.exists(categories_path):
        print(f"Error: categories.json not found at {categories_path}")
        sys.exit(1)
    categories = load_categories(categories_path)

    paths = sys.argv[1:]
    all_errors = []

    for path in paths:
        # If only a file name is given, look for it in app/data/
        if not os.path.isabs(path) and not os.path.dirname(path):
            abs_path = os.path.join(data_dir, path)
        else:
            abs_path = os.path.abspath(path)

        if os.path.isdir(abs_path):
            for fname in os.listdir(abs_path):
                if fname.endswith(".json"):
                    snippet_path = os.path.join(abs_path, fname)
                    result = validate_snippet_file(snippet_path, categories)
                    if result:
                        all_errors.extend(result)
        else:
            result = validate_snippet_file(abs_path, categories)
            if result:
                all_errors.extend(result)

    if all_errors:
        print("Validation failed with the following errors:")
        for err in all_errors:
            print("-", err)
        sys.exit(1)
    else:
        print("All snippet files validated successfully!")


if __name__ == "__main__":
    main()
