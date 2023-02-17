from flask import Flask
from app.models.meal_plan import create_meal_plan
from app.models.meal_recipe import generate_meal_recipes
from app.infra.celery_config import celery
from app.infra import logger


app = Flask(__name__)
logger.logger.debug('flask app initiated in celery')


@celery.task
def make_meal_plan_task(login):
    logger.logger.debug('celery sending meal plan request')
    create_meal_plan(login)


@celery.task
def generate_recipes_task(login):
    logger.logger.debug('celery sending recipe request')
    generate_meal_recipes(login)
