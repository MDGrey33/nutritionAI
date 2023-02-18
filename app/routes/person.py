from fastapi import APIRouter, Depends
from app.models.person import Person
from app.schemas.person import PersonCreate
from app.infra import logger

logger.logger.debug('person routes loaded')

router = APIRouter()


@router.post("/person")
async def add_new_person(person: PersonCreate):
    # Create a new Person object
    new_person = Person(name=person.name, login=person.login, gender=person.gender, height=person.height,
                        weight=person.weight, age=person.age, activity_level=person.activity_level,
                        diet=person.diet, meals_per_day=person.meals_per_day, other_notes=person.other_notes)

    # Add the new Person object to the database
    new_person.create()

    # Return a JSON response with a success message
    return {"message": "Person added"}
