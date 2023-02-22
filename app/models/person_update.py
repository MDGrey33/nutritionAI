from pydantic import BaseModel
from pydantic import validator
from typing import Optional


class PersonUpdate(BaseModel):
    name: Optional[str]
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