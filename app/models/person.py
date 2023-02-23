from pydantic import BaseModel
from pydantic import validator
from fastapi import HTTPException
from typing import Optional
from typing import List
import os
import json
from app.infra.file import File


class Person(BaseModel):
    name: Optional[str]
    login: Optional[str]
    gender: Optional[str]
    height: Optional[float]
    weight: Optional[float]
    age: Optional[int]
    activity_level: Optional[str]
    diet: Optional[str]
    meals_per_day: Optional[int]
    other_notes: Optional[str]

    @validator('height')
    def height_must_be_within_reasonable_range(cls, value):
        if not (50 <= value <= 300):
            raise ValueError(f"height must be within the range of 50 cm and 300 cm")
        return value

    @validator('weight')
    def weight_must_be_within_reasonable_range(cls, value):
        if not (0 <= value <= 400):
            raise ValueError(f"weight must be within the range of 0 kg and 400 kg")
        return value

    @validator('age')
    def age_must_be_within_reasonable_range(cls, value):
        if value <= 0 or value > 120:
            raise ValueError('age must be a positive number less than or equal to 120 years')
        return value

    def to_json(self):
        return self.dict()

    def to_dict(self):
        return self.dict()

    def get_profile_path(self):
        file = File(path=f"content/{self.login}/", name="profile.json")
        return file.get_path()

    def save(self):
        file = File(path=f"content/{self.login}/", name="profile.json")
        file.write(self.to_json(), 'w')

    @classmethod
    def read(cls, login):
        file_path = f"content/{login}/profile.json"
        if not os.path.exists(file_path):
            return None
        with open(file_path) as f:
            data = json.load(f)
            return cls.parse_obj(data)

    def update(self, update_fields: List[str]):
        person = self.read(self.login)
        if person is None:
            raise HTTPException(status_code=404, detail="Person not found")
        person_dict = person.to_dict()
        for field in update_fields:
            if field in person_dict:
                setattr(person, field, getattr(self, field))
        person.save()
        return person

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "login": "johndoe",
                "gender": "male",
                "height": 175,
                "weight": 70.0,
                "age": 30,
                "activity_level": "active",
                "diet": "paleo",
                "meals_per_day": 3,
                "other_notes": "Likes to swim",
            }
        }
        orm_mode = True
        extra = "ignore"
