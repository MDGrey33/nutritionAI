from pydantic import BaseModel, Field, confloat, conint, constr, validator


class PersonCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="The name of the person (1-50 characters)")
    login: str = Field(..., min_length=1, max_length=50, description="The login ID of the person (1-50 characters)")
    gender: str = Field(..., regex='^(male|female)$', description="The gender of the person ('male' or 'female')")
    height: float = Field(..., gt=50, le=300, description="The height of the person in centimeters (50-300 cm)")
    weight: float = Field(..., gt=0, le=400, description="The weight of the person in kilograms (0-400 kg)")
    age: int = Field(..., gt=0, le=120, description="The age of the person in years (0-120 years)")
    activity_level: str = Field(..., regex='^(sedentary|lightly active|moderately active|very active)$',
                                description="The activity level of the person ('sedentary', 'lightly active', 'moderately active', or 'very active')")
    diet: str = Field(..., min_length=1, max_length=50, description="The dietary preference of the person(1-50 characters)")
    meals_per_day: int = Field(..., gt=0, le=10, description="The number of meals the person has per day (0-10 meals)")
    other_notes: str = Field(None, max_length=500, description="Any other notes about the person (up to 500 characters)")

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
