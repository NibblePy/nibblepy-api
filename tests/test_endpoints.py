from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_snippet():
    response = client.get("/snippet?topic=list_comprehension")
    assert response.status_code == 200
    assert "code" in response.json() or "title" in response.json()
