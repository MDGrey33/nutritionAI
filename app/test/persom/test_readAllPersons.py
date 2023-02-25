from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_all_persons():
    # create a test person to make sure at least one person exists in the system
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
        "other_notes": "Likes to swim"
    }
    client.post("/persons/", json=payload)
    # get all persons
    response = client.get("/persons/")

    # delete the person created for the test
    client.delete("/persons/testperson/")

    # assert the response code and that the system has at least one person
    assert response.status_code == 200
    assert len(response.json()) > 0
