# 🧰 Contributing to NibblePy

Thank you for considering contributing to **NibblePy**!  
We welcome all types of contributions — from code to documentation and everything in between.

---

## ✍️ Contributing a Snippet

To add a new snippet:

1. Open `app/data/snippets.json`
2. Follow this format:

```json
{
"your_unique_snippet_id": {
  "title": "Your Snippet Title",
  "code": "example_code_here()",
  "explanation": "Brief explanation of what the code does.",
  "difficulty": "beginner | intermediate | advanced",
  "related": ["related_concept1", "related_concept2"],
  "category": "e.g., data types, control flow, functions"
  }
}
```
3. Run `tests/test_snippets.py` to ensure formatting is correct.
4. Commit and open a pull request with a clear description.

---

## 💡 Other Ways to Contribute
- Improve or refactor the FastAPI backend
- Add or expand test coverage (pytest)
- Add documentation or improve snippet explanations
- Suggest new categories, structure, or endpoints

---

## 🧪 Running Locally & Testing

1. Clone this repo:
```
git clone https://github.com/piotr-daniel/nibblepy.git
cd nibblepy
```

2. Install dependencies:
```
python -m venv .venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

3. Run the server:
```
uvicorn app.main:app --reload
```

4. Run tests:
```
pytest
```

---

## 🙏 Thank You!
Your contribution helps learners around the world build strong Python foundations. We’re glad to have you here! 🎉