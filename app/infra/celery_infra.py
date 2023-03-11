"""app.infra.celery_infra"""
from celery import Celery
from dotenv import load_dotenv
import os
from redis.exceptions import ConnectionError
from app.infra import logger

CELERY_IMPORTS = ('app.routes.meal', )

load_dotenv()
REDIS_CONNECTION_STRING = os.getenv("REDIS_CONNECTION_STRING")

celery_app = Celery(
    "tasks", broker=REDIS_CONNECTION_STRING, backend=REDIS_CONNECTION_STRING
)

try:
    celery_app.connection()
    logger.logger.debug('Celery broker and backend connections are OK')
except ConnectionError as ex:
    logger.logger.error(f'Error connecting to Redis: {str(ex)}')
    raise

from app.models.meal import MealPlan
from app.infra.gpt import ask_gpt


@celery_app.task
async def generate_meal_plan(person_login: str, prompt: str):
    try:
        # Call OpenAI's API to generate a meal plan
        logger.logger.info(f"Sending request to GPT for meal plan generation for person {person_login}")
        response = await ask_gpt(prompt)

        # Parse the meal plan from the API response
        meal_plan = MealPlan.parse_raw(response)

        logger.logger.info(f"Writing meal plan to file for person {person_login}")
        # Save the meal plan to a file
        meal_plan.save(person_login)

        logger.logger.debug("Meal plan generated successfully")
    except Exception as e:
        logger.logger.error(str(e))

