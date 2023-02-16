from flask import request
from app import app
from celery.result import AsyncResult
from app.infra.celery_config import celery
from app.infra import logger
from app.models.person import Person
from app.infra.app_celery import generate_recipes_task, make_meal_plan_task


def add_person_object(data):
    person = Person(name=data["name"],
                    login=data["login"],
                    gender=data["gender"],
                    height=data["height"],
                    weight=data["weight"],
                    age=data["age"],
                    activity_level=data["activity_level"],
                    diet=data["diet"],
                    meals_per_day=data["meals_per_day"],
                    other_notes=data["other_notes"])
    logger.logger.debug(f"{person.name} Person object created")
    person.create()
    logger.logger.debug(f"{person.name} Person object added to json")
    return {"message": "Person added"}


def generate_recipes(login):
    task_id = request.args.get('task_id')
    task = AsyncResult(task_id, app=celery)
    if task.state == 'SUCCESS':
        result = generate_recipes_task.apply_async(args=[login])
        logger.logger.debug("Meal recipes task added to queue, task id: {}".format(result.id))
        return "Meal recipes task added to queue, task id: {}".format(result.id)
    else:
        logger.logger.debug("Meal plan not completed yet, task id: {}".format(task_id))
        return "Meal plan not completed yet, task id: {}".format(task_id)


logger.logger.debug("Defining routes")


@app.route("/person", methods=["POST"])
def add_new_person_route():
    logger.logger.debug("Add new person route summoned")
    data = request.get_json()
    return add_person_object(data)


@app.route("/meal_plan/<string:login>", methods=["GET"])
def make_meal_plan_route(login):
    logger.logger.debug("make meal plan route summoned")
    task = make_meal_plan_task.apply_async(args=[login])
    return "Meal plan task added to queue, task id: {}".format(task.id)


@app.route("/generate_recipes/<string:login>", methods=["GET"])
def generate_recipes_route(login):
    logger.logger.debug("generate recipes route summoned")
    return generate_recipes(login)


