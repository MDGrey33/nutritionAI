import os
import json
from fastapi.testclient import TestClient
from app.routes.meal import meal_router


client = TestClient(meal_router)


def test_create_meal_plan():
    # Arrange
    login = 'testperson'
    path = f'content/{login}'
    os.makedirs(path, exist_ok=True)
    with open(f'{path}/profile.json', 'w') as f:
        profile_data = {
            "name": "Test Person",
            "login": login,
            "gender": "male",
            "height": 180.0,
            "weight": 75.0,
            "age": 25,
            "activity_level": "active",
            "diet": "paleo",
            "meals_per_day": 3,
            "other_notes": "Likes to swim"
        }
        json.dump(profile_data, f)

    # Act
    response = client.post('/meal-plans/', json={'person_login': login})

    # Assert
    assert response.status_code == 200
    assert 'task id' in response.text

    # Assert meal plan file was created
    assert os.path.exists(f'{path}/meal_plan.json')

    # Assert meal plan file contains expected keys
    with open(f'{path}/meal_plan.json', 'r') as f:
        meal_plan_data = json.load(f)
        assert all(key in meal_plan_data for key in ['day', 'meals', 'NutritionSummary'])
        assert all(key in meal for meal in meal_plan_data['meal_plan'] for key in ['type', 'name', 'servings', 'nutrition_facts'])
        assert all(key in meal['nutrition_facts'] for meal in meal_plan_data['meal_plan'] for key in ['calories', 'fat', 'carbohydrates', 'protein'])

    # Clean up
    os.system(f'rm -rf {path}')
