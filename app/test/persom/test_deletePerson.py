from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_delete_person():
    # create a test person to delete
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

    # delete the test person
    response = client.delete("/persons/testperson/")
    assert response.status_code == 200

    # make sure the person is deleted
    response = client.get("/persons/testperson/")
    assert response.status_code == 404
