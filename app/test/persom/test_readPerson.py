from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_person():
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

    # read the test person
    response = client.get("/persons/testperson/")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Person"
    assert response.json()["login"] == "testperson"
    assert response.json()["gender"] == "male"
    assert response.json()["height"] == 180
    assert response.json()["weight"] == 75.0
    assert response.json()["age"] == 25
    assert response.json()["activity_level"] == "active"
    assert response.json()["diet"] == "paleo"
    assert response.json()["meals_per_day"] == 3
    assert response.json()["other_notes"] == "Likes to swim"

