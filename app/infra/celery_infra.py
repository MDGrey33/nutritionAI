"""app.infra.celery_infra"""
from celery import Celery
from dotenv import load_dotenv
import os
from redis.exceptions import ConnectionError
from app.infra.logger import logger
from app.routes.meal_prompt import create_meal_plan

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


@celery_app.task
def generate_meal_plan(person_login: str):
    create_meal_plan(person_login)



