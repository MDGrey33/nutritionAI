from fastapi import APIRouter, HTTPException
from typing import List
from app.models.person_update import PersonUpdate
from app.models.person_create import PersonCreate
from app.models.person import Person
import os
import json
from app.infra import logger

persons_router = APIRouter()


@persons_router.get("/persons/", response_model=List[Person])
async def read_persons(skip: int = 0, limit: int = 100):
    persons = []
    for dir_name in os.listdir("content"):
        person_file_path = os.path.join("content", dir_name, "profile.json")
        if os.path.isfile(person_file_path):
            with open(person_file_path) as f:
                data = json.load(f)
                persons.append(Person.parse_obj(data))
    return persons[skip : skip + limit]


@persons_router.post("/persons/", response_model=Person)
async def create_person(person: PersonCreate):
    person_dir_path = os.path.join("content", person.login)
    if os.path.exists(person_dir_path):
        raise HTTPException(status_code=400, detail="User already exists")
    new_person = Person(**person.dict())
    os.makedirs(person_dir_path)
    new_person.save()
    return new_person


@persons_router.get("/persons/{person_login}", response_model=Person)
async def read_person(person_login: str):
    person = Person.read(person_login)
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person


@persons_router.put("/persons/{person_login}", response_model=Person)
async def update_person(person_login: str, person: PersonUpdate):
    existing_person = Person.read(person_login)
    if existing_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    person_dict = person.dict(exclude_unset=True)
    for field in person_dict:
        setattr(existing_person, field, person_dict[field])
    existing_person.save()
    return existing_person


@persons_router.delete("/persons/{person_login}")
async def delete_person(person_login: str):
    existing_person = Person.read(person_login)
    if existing_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    file_path = existing_person.get_file_path()
    os.remove(file_path)
    os.rmdir(os.path.dirname(file_path))
    return {"message": "Person deleted successfully"}
