from flask import Flask
from app.models.meal_plan import create_meal_plan
from app.models.meal_recipe import generate_meal_recipes
from app.infra.celery_config import celery
from app.infra import logger


app = Flask(__name__)


@celery.task
def make_meal_plan_task(login):
    create_meal_plan(login)


@celery.task
def generate_recipes_task(login):
    generate_meal_recipes(login)
