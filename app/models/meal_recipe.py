import json
import os
from app.infra.gpt import ask_gpt
from app.infra.file_system import write_file
from app.models.meal_recipe_message import get_conversation
from app.models.person import Person
from app.infra import logger


def generate_meal_recipes(login):
    # get person based on login
    person = Person.read("", login)
    if person:
        logger.logger.debug('person read successfully from JSON')
        weekly_plan_path = '{}/weekly_plan.json'.format(person.profile_path)
        meals_path = '{}/week1/'.format(person.profile_path)
        progress_file_path = '{}/progress.json'.format(meals_path)

        if not os.path.exists(meals_path):
            os.makedirs(meals_path)
            logger.logger.debug(f'{meals_path} not found and created successfully ')
        progress = []
        if os.path.exists(progress_file_path):
            with open(progress_file_path, 'r') as progress_file:
                progress = json.load(progress_file)
                logger.logger.debug(f'{progress_file_path} progress file found and loaded')

        with open(weekly_plan_path, 'r') as f:
            meal_plan_data = json.load(f)
            logger.logger.debug(f'meal plan {weekly_plan_path} loaded')
        for day in meal_plan_data['meal_plan']:
            for meal in day['meals']:
                if meal['name'] not in progress:
                    conversation = get_conversation(meal)
                    logger.logger.debug(f'Meal recipe requested from chat OpenAI')
                    response = ask_gpt(conversation)
                    logger.logger.debug(f'response received from OpenAI')
                    meal_file_path = '{}{}_recipe.json'.format(meals_path, meal['name'])
                    write_file(response, meal_file_path)
                    logger.logger.debug(f'{meal_file_path} is written')
                    progress.append(meal['name'])
                    with open(progress_file_path, 'w') as progress_file:
                        json.dump(progress, progress_file)
                    logger.logger.debug(f'{meal["name"]} added to {progress_file_path}')
    else:
        pass
        logger.logger.debug("Person not found.")
