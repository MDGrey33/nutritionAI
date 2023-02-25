from pydantic import BaseModel
from pydantic import validator


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
    cookingTime: float
    ingredient: [Ingredient]
    instructions: [str]

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


class MealPlan(BaseModel):
    day: str
    meals: [Meal]
    nutrition_facts: NutritionFacts
