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
    assert "category" in response.json()


def test_fetch_all_snippets():
    response = client.get("/snippets")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert "title" in response.json()[next(iter(response.json()))]
    assert "category" in response.json()[next(iter(response.json()))]


def test_list_categories():
    response = client.get("/categories")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_list_difficulties():
    response = client.get("/difficulties")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
