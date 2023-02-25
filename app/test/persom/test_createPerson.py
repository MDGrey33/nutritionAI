from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_person():

    # Test creating a person that doesn't exist in the system
    # Make sure the test person is not already in the system
    client.delete("/persons/johndoe/")

    # Prepare the payload
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

    # Create the person
    response = client.post("/persons/", json=data)

    # Test asserts
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
