from pydantic import BaseModel, confloat, conint, constr, validator, Field


class PersonCreate(BaseModel):
    name: constr(min_length=1, max_length=50)
    login: constr(min_length=1, max_length=50)
    gender: constr(regex='^(male|female)$')
    height: confloat(gt=50, le=300)
    weight: confloat(gt=0, le=400)
    age: conint(gt=0, le=120)
    activity_level: constr(regex='^(sedentary|lightly active|moderately active|very active)$')
    diet: str
    meals_per_day: conint(gt=0, le=10)
    other_notes: constr(max_length=500)

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

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "login": "johndoe",
                "gender": "male",
                "height": 180,
                "weight": 80,
                "age": 30,
                "activity_level": "moderately active",
                "diet": "omnivore",
                "meals_per_day": 3,
                "other_notes": "Likes spicy food."
            }
        }
        description = "Create a new person with the given attributes. `height`, `weight`, and `age` should be " \
                      "positive numbers, and `height` should be less than or equal to 300 cm, `weight` should be less " \
                      "than or equal to 400 kg, and `age` should be less than or equal to 120 years. "
