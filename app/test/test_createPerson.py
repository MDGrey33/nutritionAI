from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_person():
    # Test creating a new person
    data = {
        "name": "John Doe",
        "login": "johndoe",
        "gender": "male",
        "height": 175,
        "weight": 70.0,
        "age": 30,
        "activity_level": "active",
        "diet": "paleo",
        "meals_per_day": 3,
        "other_notes": "Likes to swim"
    }
    response = client.post("/persons/", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "name": "John Doe",
        "login": "johndoe",
        "gender": "male",
        "height": 175,
        "weight": 70.0,
        "age": 30,
        "activity_level": "active",
        "diet": "paleo",
        "meals_per_day": 3,
        "other_notes": "Likes to swim"
    }

    # Test creating a person with the same login as an existing person
    response = client.post("/persons/", json=data)
    client.delete("/persons/johndoe/")
    assert response.status_code == 400
