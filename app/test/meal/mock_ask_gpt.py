from app.infra.file import File

# Mock code only used when the gpt import is commented to test
def ask_gpt(prompt):
    meal_plan = {
        "meal_plan": [
            {
                "day": "Monday",
                "meals": [
                    {
                        "type": "Breakfast",
                        "name": "Keto Omelette",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 435,
                            "fat": 36,
                            "carbohydrates": 2.5,
                            "protein": 25
                        }
                    },
                    {
                        "type": "Lunch",
                        "name": "Keto Bunless Burger",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 470,
                            "fat": 32,
                            "carbohydrates": 0.8,
                            "protein": 37
                        }
                    },
                    {
                        "type": "Dinner",
                        "name": "Keto Chicken Stir Fry",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 750,
                            "fat": 51,
                            "carbohydrates": 7.3,
                            "protein": 42
                        }
                    }
                ],
                "NutritionSummary": {
                    "calories": 1655,
                    "fat": 119,
                    "carbohydrates": 10.6,
                    "protein": 104
                }
            },
            {
                "day": "Tuesday",
                "meals": [
                    {
                        "type": "Breakfast",
                        "name": "Keto Smoothie Bowl",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 510,
                            "fat": 42,
                            "carbohydrates": 7,
                            "protein": 25
                        }
                    },
                    {
                        "type": "Lunch",
                        "name": "Keto Caesar Salad",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 330,
                            "fat": 28,
                            "carbohydrates": 6,
                            "protein": 18
                        }
                    },
                    {
                        "type": "Dinner",
                        "name": "Keto Salmon and Asparagus",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 600,
                            "fat": 45,
                            "carbohydrates": 8,
                            "protein": 35
                        }
                    }
                ],
                "NutritionSummary": {
                    "calories": 1440,
                    "fat": 115,
                    "carbohydrates": 21,
                    "protein": 78
                }
            },
            {
                "day": "Wednesday",
                "meals": [
                    {
                        "type": "Breakfast",
                        "name": "Keto Avocado Toast",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 530,
                            "fat": 44,
                            "carbohydrates": 9,
                            "protein": 10
                        }
                    },
                    {
                        "type": "Lunch",
                        "name": "Keto Cobb Salad",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 480,
                            "fat": 38,
                            "carbohydrates": 4,
                            "protein": 30
                        }
                    },
                    {
                        "type": "Dinner",
                        "name": "Keto Steak Fajitas",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 630,
                            "fat": 42,
                            "carbohydrates": 7,
                            "protein": 43
                        }
                    }
                ],
                "NutritionSummary": {
                    "calories": 1640,
                    "fat": 124,
                    "carbohydrates": 20,
                    "protein": 83
                }
            },
            {
                "day": "Thursday",
                "meals": [
                    {
                        "type": "Breakfast",
                        "name": "Keto Egg Muffins",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 425,
                            "fat": 34,
                            "carbohydrates": 1.5,
                            "protein": 22
                        }
                    },
                    {
                        "type": "Lunch",
                        "name": "Keto Spaghetti Squash with Meat Sauce",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 440,
                            "fat": 27,
                            "carbohydrates": 11,
                            "protein": 24
                        }
                    },
                    {
                        "type": "Dinner",
                        "name": "Keto Pork Chops with Brussels Sprouts",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 640,
                            "fat": 48,
                            "carbohydrates": 8,
                            "protein": 34
                        }
                    }
                ],
                "NutritionSummary": {
                    "calories": 1505,
                    "fat": 109,
                    "carbohydrates": 20.5,
                    "protein": 80
                }
            },
            {
                "day": "Friday",
                "meals": [
                    {
                        "type": "Breakfast",
                        "name": "Keto Pancakes",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 490,
                            "fat": 39,
                            "carbohydrates": 3,
                            "protein": 24
                        }
                    },
                    {
                        "type": "Lunch",
                        "name": "Keto Grilled Cheese Sandwich",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 470,
                            "fat": 36,
                            "carbohydrates": 2,
                            "protein": 22
                        }
                    },
                    {
                        "type": "Dinner",
                        "name": "Keto Cauliflower Pizza",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 620,
                            "fat": 46,
                            "carbohydrates": 9,
                            "protein": 33
                        }
                    }
                ],
                "NutritionSummary": {
                    "calories": 1580,
                    "fat": 121,
                    "carbohydrates": 14,
                    "protein": 79
                }
            },
            {
                "day": "Saturday",
                "meals": [
                    {
                        "type": "Breakfast",
                        "name": "Keto Baked Eggs",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 425,
                            "fat": 32,
                            "carbohydrates": 4,
                            "protein": 23
                        }
                    },
                    {
                        "type": "Lunch",
                        "name": "Keto Sushi Bowl",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 440,
                            "fat": 32,
                            "carbohydrates": 8,
                            "protein": 20
                        }
                    },
                    {
                        "type": "Dinner",
                        "name": "Keto Broiled Salmon",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 540,
                            "fat": 35,
                            "carbohydrates": 5,
                            "protein": 38
                        }
                    }
                ],
                "NutritionSummary": {
                    "calories": 1405,
                    "fat": 99,
                    "carbohydrates": 17,
                    "protein": 81
                }
            },
            {
                "day": "Sunday",
                "meals": [
                    {
                        "type": "Breakfast",
                        "name": "Keto Breakfast Burrito",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 500,
                            "fat": 40,
                            "carbohydrates": 2,
                            "protein": 24
                        }
                    },
                    {
                        "type": "Lunch",
                        "name": "Keto Cobb Salad",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 480,
                            "fat": 38,
                            "carbohydrates": 4,
                            "protein": 30
                        }
                    },
                    {
                        "type": "Dinner",
                        "name": "Keto Steak and Veggies",
                        "servings": 1,
                        "nutrition_facts": {
                            "calories": 560,
                            "fat": 39,
                            "carbohydrates": 5,
                            "protein": 40
                        }
                    }
                ],
                "NutritionSummary": {
                    "calories": 1540,
                    "fat": 117,
                    "carbohydrates": 11,
                    "protein": 94
                }
            }
        ]
    }
    return meal_plan

def create_meal_plan(login):
    meal_plan = ask_gpt(prompt='mock text')
    meal_plan_file = File(path=f"content/{login}", name="meal_plan.json")
    meal_plan_file.write(data=meal_plan, mode='w')


create_meal_plan("rolandabouyounes")