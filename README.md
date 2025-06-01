# 🐍 NibblePy — Python Snippet API

> A fast and clean REST API serving beginner-friendly Python code snippets with explanations, difficulty levels, and related concepts.

---

## 🚀 Overview

NibblePy helps learners discover Python fundamentals through small, well-explained code snippets.  
Each snippet includes:

- ✅ Code example
- 📘 Clear explanation
- 🏷️ Tags and difficulty level
- 🔗 Related concepts

Built using **FastAPI**, this project is open for contributions from educators, learners, and developers alike.

---

## 📦 Example Snippet

```json
{
  "title": "Variables and Basic Data Types",
  "code": "x = 5\nname = 'Alice'\nis_active = True\npi = 3.14",
  "explanation": "Shows how to create variables with different data types: integer, string, boolean, float.",
  "difficulty": "beginner",
  "related": ["conditionals", "functions", "list_operations"]
}

```

---

## Contributing

1. Open app/snippets.json
2. Add a new entry using the format below:

```json
{
  "title": "Your Snippet Title",
  "code": "example_code_here()",
  "explanation": "Brief explanation of what the code does.",
  "difficulty": "beginner | intermediate | advanced",
  "related": ["related_concept1", "related_concept2"]
}
```
3. Open a pull request with your changes.

📌 No coding or testing experience needed — just contribute meaningful and accurate Python snippets!