from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_all_fruits():
    response = client.get("/fruits")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_fruit():
    response = client.post("/fruits", json={"fruit": "banana", "color": "yellow"})
    assert response.status_code == 200
    data = response.json()
    assert data["fruit"] == "banana"
    assert data["color"] == "yellow"
    assert "id" in data
