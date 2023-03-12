"""app.infra.celery_infra"""
from celery import Celery
from dotenv import load_dotenv
import os
from redis.exceptions import ConnectionError
from app.infra.logger import logger

CELERY_IMPORTS = ('app.routes.meal', )

load_dotenv()
REDIS_CONNECTION_STRING = os.getenv("REDIS_CONNECTION_STRING")

celery_app = Celery(
    "tasks", broker=REDIS_CONNECTION_STRING, backend=REDIS_CONNECTION_STRING
)

try:
    celery_app.connection()
    logger.debug('Celery broker and backend connections are OK')
except ConnectionError as ex:
    logger.error(f'Error connecting to Redis: {str(ex)}')
    raise

from app.models.meal import MealPlan
from app.infra.gpt import ask_gpt


@celery_app.task
async def generate_meal_plan(person_login: str, prompt: str):
    # Call OpenAI's API to generate a meal plan
    ask_gpt(prompt)
    """
    # Wait for the response to complete and retrieve its content as bytes
    result_bytes = await response.content.read()

    # Decode the bytes to a string
    result_str = result_bytes.decode('utf-8')

    # Parse the meal plan from the API response
    meal_plan = MealPlan.parse_raw(result_str)

    # Save the meal plan to a file
    meal_plan.save(person_login)
    """


