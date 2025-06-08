# Contributing to NibblePy Snippet API

Thank you for your interest in contributing! 🎉  
We welcome all contributions that help expand and improve our collection of Python code snippets.

---

## 🚀 Quick Start

1. **Fork this repository and clone your fork locally.**
2. **Create a new snippet JSON file in the `data/` directory.**
3. **Name your file using lowercase letters, numbers, and hyphens (`-`) only.**
   - Example: `list-creation-basic.json`
   - Avoid spaces, underscores, or special characters.
4. **Copy and use the template from `data/_TEMPLATE.json` as a starting point.**
5. **Fill in all required fields:**
   - `title`: A concise, descriptive title.
   - `code`: The code snippet (use `\n` for newlines).
   - `explanation`: A clear explanation of what the code does.
   - `difficulty`: One of `beginner`, `intermediate`, or `advanced`.
   - `category`: A relevant category (e.g., "Data Structures", "File I/O").
6. **(Optional) Validate your JSON file using the provided script:**
   ```sh
   python scripts/validate_snippets.py data/your-snippet-file.json
   ```
7. **Open a Pull Request (PR) describing your snippet and its value.**
8. **Do not edit or submit the SQLite database.**  
   The database is updated from JSON by maintainers after PRs are merged.

---

## 📄 Snippet JSON Template

Copy the following template (or use `data/_TEMPLATE.json`):

```json
{
  "title": "Descriptive Snippet Title",
  "code": "your_code_here  # optional inline comments",
  "explanation": "Clear, concise explanation.",
  "difficulty": "beginner | intermediate | advanced",
  "category": "Meaningful Category Name"
}
```

**Example:**

```json
{
  "title": "List Creation and Basic Operations",
  "code": "fruits = ['apple', 'banana', 'cherry']\\nfruits.append('plum')\\nprint(fruits[1])\\nfruits.remove('apple')\\nfruits.sort(reverse=True)",
  "explanation": "Creates a list, appends an item, accesses an element by index, removes an item, and sorts the list in descending order.",
  "difficulty": "beginner",
  "category": "Data Structures"
}
```

---

## 📝 Guidelines

- **Each snippet must be in its own file** in `data/`, with a unique name.
- **File names should use hyphens:**  
  ✅ `list-creation-basic.json`  
  ❌ `list_creation_basic.json`  
  ❌ `List Creation Basic.json`
- **All fields are required** and must follow the template.
- **Difficulty** must be one of: `beginner`, `intermediate`, `advanced`.
- **Category** should be concise and match similar existing snippets if possible.

---

## ✅ Before You Submit

- [ ] File is in `data/` and uses hyphens for the name.
- [ ] All required fields are filled.
- [ ] Difficulty is valid (`beginner`, `intermediate`, `advanced`).
- [ ] (Optional) File passes validation script.
- [ ] You did **not** edit the database file.

---

## 🔎 Reviewing & Merging

- Maintainers will review your PR.
- If changes are needed, maintainers will comment with suggestions.
- Once approved, your snippet will be merged, and the database will be updated by running the sync script.

---

## 💬 Questions?

Feel free to open an issue or start a discussion if you have questions or suggestions!

Thank you for helping grow the NibblePy Snippet API community! 🚀🐍