from app.infra import logger


json_template_other = """{
    "meal_plan": [
        {
            "day": "Monday",
            "meals": [
                {
                    "type": "Meal one",
                    "name": "Omlette",
                    "servings": "2 omlettes",
                    "nutrition_facts": {
                        "calories": 450,
                        "fat": 30,
                        "carbohydrates": 2,
                        "protein": 25
                    }
                },
                {
                    "type": "Meal Two",
                    ...
                }
            ],
            "NutritionSummary": {
                "calories": 1350,
                "fat": 85,
                "carbohydrates": 7,
                "protein": 80
            }
        },
        {
            "day": "Tuesday",
            ...
        },
        {
            "day": "Wednesday",
            ...
        }
        {
            "day": "Thursday",
            ...
        }
        {
            "day": "Friday",
            ...
        }
        {
            "day": "Saturday",
            ...
        }
        {
            "day": "Sunday",
            ...
        }
    ]
}"""

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
                        "calories": number ,
                        "fat": number,
                        "carbohydrates": number,
                        "protein": number
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
                "calories": number,
                "fat": number,
                "carbohydrates": number,
                "protein": number
            }
        },
        {
            "day": "Tuesday",
            ...
        },
        {
            "day": "Wednesday",
            ...
        }
        {
            "day": "Thursday",
            ...
        }
        {
            "day": "Friday",
            ...
        }
        {
            "day": "Saturday",
            ...
        }
        {
            "day": "Sunday",
            ...
        }
    ]
}"""


def get_conversation(person, tdee):
    # Check if other notes is used
    if person.other_notes:
        other = f'account for: {person.other_notes}'
    else:
        other = ''

    if person.meals_per_day == "3":
        json_template = json_template_three_meals
        logger.logger.debug('3 meal plan found')
    else:
        json_template = json_template_other

    conversation = f"""Generate a weekly meal plan in the following JSON Format
The plan should be optimal for one person with the following parameters: 
diet: {person.diet}, gender: {person.gender}, height: {person.height}, weight: {person.weight}, age: {person.age}, activity level: {person.activity_level}. 
{other}  
The plan should be delivered using the provided JSON format and constraints below:
Each meal includes a name, serving size and nutritional information.
The nutritional information includes the total calories, fat, carbohydrates and protein.
The plan should include {person.meals_per_day} meals for 7 days with a total calorie count for each day.
Daily calory count should be based on TDEE {tdee}
Use 
{json_template}
"""
    logger.logger.debug('Conversation generated')
    return conversation
