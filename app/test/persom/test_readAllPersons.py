from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_all_persons():
    # create a test person to read
    payload = {
        "name": "Test Person",
        "login": "testperson",
        "gender": "male",
        "height": 180,
        "weight": 75.0,
        "age": 25,
        "activity_level": "active",
        "diet": "paleo",
        "meals_per_day": 3,
        "other_notes": "Likes to swim",
    }
    client.post("/persons/", json=payload)
    response = client.get("/persons/")
    client.delete("/persons/testperson/")
    assert response.status_code == 200
    assert len(response.json()) > 0
