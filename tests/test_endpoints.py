from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_snippet():
    response = client.get("/snippet?topic=dictionaries")
    assert response.status_code == 200
    assert "title" in response.json()
    assert "code" in response.json()
    assert "explanation" in response.json()
    assert "difficulty" in response.json()
    assert "related" in response.json()
