import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.person import Person
from app.models.person_update import PersonUpdate
import os

client = TestClient(app)


@pytest.fixture
def person():
    person_dict = {
        "name": "Jane Doe",
        "login": "janedoe",
        "gender": "female",
        "height": 165.0,
        "weight": 60.0,
        "age": 25,
        "activity_level": "moderately active",
        "diet": "vegetarian",
        "meals_per_day": 3,
        "other_notes": "Likes to run",
    }
    person = Person(**person_dict)
    person_dir_path = os.path.join("content", person.login)
    if not os.path.exists(person_dir_path):
        os.makedirs(person_dir_path)
    person.save()
    yield person
    os.remove(person.get_profile_path())
    os.rmdir(os.path.dirname(person.get_profile_path()))


def test_update_person(person):
    new_person_dict = {
        "name": "Jane Austen",
        "login": "janedoe",
        "gender": "female",
        "height": 170.0,
        "weight": 65.0,
        "age": 30,
        "activity_level": "active",
        "diet": "vegan",
        "meals_per_day": 2,
        "other_notes": "Likes to swim",
    }
    update_fields = list(new_person_dict.keys())
    new_person = PersonUpdate(**new_person_dict)
    response = client.put(f"/persons/{person.login}/", json=new_person.dict())
    assert response.status_code == 200
    assert response.json() == Person.parse_obj(new_person_dict).dict()
    person = Person.read(person.login)
    for key, value in new_person_dict.items():
        assert getattr(person, key) == value
    person.update(update_fields)
