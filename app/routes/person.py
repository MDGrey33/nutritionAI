import pydantic
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from app.models.person_update import PersonUpdate
from app.models.person_create import PersonCreate
from app.models.person import Person
import os
import json
from app.infra.logger import logger
import shutil


persons_router = APIRouter()


@persons_router.get("/persons/", response_model=List[Person])
async def read_persons(skip: int = 0, limit: int = 100):
    try:
        persons = []
        for dir_name in os.listdir("content"):
            person_file_path = os.path.join("content", dir_name, "profile.json")
            if os.path.isfile(person_file_path):
                with open(person_file_path) as f:
                    try:
                        data = json.load(f)
                        persons.append(Person.parse_obj(data))
                    except json.JSONDecodeError:
                        # Handle JSON decoding errors
                        return JSONResponse(content={"error": "Invalid JSON in file"}, status_code=400)
        return persons[skip: skip + limit]
    except OSError:
        # Handle missing content directory
        return JSONResponse(content={"error": "Content directory not found"}, status_code=500)
    except pydantic.ValidationError as e:
        # Handle missing required fields in Person model
        return JSONResponse(content={"error": f"Validation error: {e}"}, status_code=400)


@persons_router.post("/persons/", response_model=Person)
async def create_person(person: PersonCreate):
    person_dir_path = os.path.join("content", person.login)
    if os.path.exists(person_dir_path):
        raise HTTPException(status_code=400, detail="User already exists")

    # Create the new Person object and try to save it
    new_person = Person(**person.dict())
    try:
        os.makedirs(person_dir_path)
        new_person.save()
    except OSError:
        # Handle error creating directory
        raise HTTPException(status_code=500, detail="Could not create user directory")
    except Exception as e:
        # Handle other errors during Person creation/saving
        raise HTTPException(status_code=500, detail=f"Error creating user: {str(e)}")

    return new_person


@persons_router.get("/persons/{person_login}", response_model=Person)
async def read_person(person_login: str):
    try:
        person = Person.read(person_login)
    except Exception as e:
        # Handle errors during Person.read method call
        raise HTTPException(status_code=500, detail=f"Error reading person: {str(e)}")
    if person is None:
        # Handle case where person is not found
        raise HTTPException(status_code=404, detail="Person not found")
    return person


@persons_router.put("/persons/{person_login}", response_model=Person)
async def update_person(person_login: str, person: PersonUpdate):
    try:
        existing_person = Person.read(person_login)
    except Exception as e:
        # Handle errors during Person.read method call
        raise HTTPException(status_code=500, detail=f"Error reading person: {str(e)}")
    if existing_person is None:
        # Handle case where person is not found
        raise HTTPException(status_code=404, detail="Person not found")

    # Update the existing person object and try to save it
    person_dict = person.dict(exclude_unset=True)
    for field in person_dict:
        setattr(existing_person, field, person_dict[field])
    try:
        existing_person.save()
    except Exception as e:
        # Handle errors during Person.save method call
        raise HTTPException(status_code=500, detail=f"Error saving person: {str(e)}")

    return existing_person


@persons_router.delete("/persons/{person_login}")
async def delete_person(person_login: str):
    try:
        existing_person = Person.read(person_login)
    except Exception as e:
        # Handle errors during Person.read method call
        raise HTTPException(status_code=500, detail=f"Error reading person: {str(e)}")
    if existing_person is None:
        # Handle case where person is not found
        raise HTTPException(status_code=404, detail="Person not found")

    # Try to delete the person's directory and all files it contains
    file_path = existing_person.get_profile_path()
    try:
        shutil.rmtree(os.path.dirname(file_path))
    except Exception as e:
        # Handle errors during directory deletion
        raise HTTPException(status_code=500, detail=f"Error deleting directory: {str(e)}")

    return {"message": "Person deleted successfully"}

"""async def delete_person(person_login: str):
    try:
        existing_person = Person.read(person_login)
    except Exception as e:
        # Handle errors during Person.read method call
        raise HTTPException(status_code=500, detail=f"Error reading person: {str(e)}")
    if existing_person is None:
        # Handle case where person is not found
        raise HTTPException(status_code=404, detail="Person not found")

    # Try to delete the person's profile and directory
    file_path = existing_person.get_profile_path()
    try:
        os.remove(file_path)
    except Exception as e:
        # Handle errors during file deletion
        raise HTTPException(status_code=500, detail=f"Error deleting file: {str(e)}")
    try:
        os.rmdir(os.path.dirname(file_path))
    except Exception as e:
        # Handle errors during directory deletion
        raise HTTPException(status_code=500, detail=f"Error deleting directory: {str(e)}")

    return {"message": "Person deleted successfully"}
"""

logger.debug("app.routes.person file end reached")
