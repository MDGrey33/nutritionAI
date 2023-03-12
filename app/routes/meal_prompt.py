from app.infra.gpt import ask_gpt
from app.infra.file import File
from app.models.person import Person
from app.infra.logger import logger
import json

json_template_three_meals = """{
    "meal_plan": [
        {
            "day": "Monday",
            "meals": [
                {
                    "type": "Breakfast",
                    "name": "mealname",
                    "servings": "number of servings",
                    "nutrition_facts": {
                        "calories": "1755" ,
                        "fat": "119",
                        "carbohydrates": "27",
                        "protein": "104"
                    }
                },
                {
                    "type": "Lunch",
                    ...
                },
                {
                    "type": "Dinner",
                    ...
                }
            ],
            "NutritionSummary": {
                "calories": "10520",
                "fat": "1190",
                "carbohydrates": "750",
                "protein": "1000"
            }
        },
        {
            "day": "Tuesday",
            ...
        },
        {
            "day": "Wednesday",
            ...
        },
        {
            "day": "Thursday",
            ...
        },
        {
            "day": "Friday",
            ...
        },
        {
            "day": "Saturday",
            ...
        },
        {
            "day": "Sunday",
            ...
        }
    ]
}"""


def generate_meal_plan_prompt(person: Person) -> str:
    # Generate a prompt that includes the user's personal details
    prompt = f"Assume you are a nutrition expert.\n"
    prompt += f"Generate a meal plan for the next week based on the following criteria:\n\n"
    prompt += f"Gender: {person.gender}\n"
    prompt += f"Height: {person.height} cm\n"
    prompt += f"Weight: {person.weight} kg\n"
    prompt += f"Age: {person.age}\n"
    prompt += f"Activity Level: {person.activity_level}\n"
    prompt += f"Diet: {person.diet}\n"
    prompt += f"Meals per Day: {person.meals_per_day}\n"
    prompt += f"Other Notes: {person.other_notes}\n\n"
    prompt += "The meal plan should be in the following format:\n\n"
    prompt += json_template_three_meals
    logger.debug("Meal plan prompt generated successfully")

    return prompt


def create_meal_plan(login):
    person = Person.read(login)
    prompt = generate_meal_plan_prompt(person)
    print(f"{prompt}")
    meal_plan = json.loads(ask_gpt(prompt))
    print(meal_plan)
    meal_plan_file = File(path=f"content/{person.login}", name="meal_plan.json")
    meal_plan_file.write(data=meal_plan, mode='w')


create_meal_plan("rolandabouyounes")
