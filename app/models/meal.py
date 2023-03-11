from typing import List
from pydantic import BaseModel, validator
from app.infra.file import File


class NutritionFacts(BaseModel):
    calories: float
    protein: float
    carbohydrates: float
    fat: float


class Ingredient(BaseModel):
    name: str
    quantity: float
    unit: str


class Recipe(BaseModel):
    name: str
    serving: float
    nutrition_facts: NutritionFacts
    cooking_time: float
    ingredients: List[Ingredient]
    instructions: List[str]

    @validator('*', pre=True)
    def check_non_negative(cls, value, field):
        if field.name in ['calories', 'fat', 'carbohydrates', 'protein'] and value < 0:
            raise ValueError(f"{field.name} must be a non-negative number")
        return value


class Meal(BaseModel):
    name: str
    servings: float
    nutrition_facts: NutritionFacts

    @validator('servings')
    def check_non_negative(cls, value):
        if value < 0:
            raise ValueError(f"nutrition_facts must be a non-negative number")
        return value


def get_meal_plan_path(person_login: str):
    return f"content/{person_login}/week1/"


class MealPlan(BaseModel):
    day: str
    meals: List[Meal]
    nutrition_facts: NutritionFacts

    def save(self, person_login: str):
        file = File(get_meal_plan_path(person_login), "meal_plan.json")
        file.write(self, 'w')

    @classmethod
    def read(cls, person_login: str):
        file = File(get_meal_plan_path(person_login), "meal_plan.json")
        meal_plan = file.read(cls)
        return meal_plan
