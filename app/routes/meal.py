"""app.routes.meal"""
from fastapi import APIRouter, HTTPException
from app.models.meal import MealPlan
from app.models.person import Person
from app.infra.logger import logger
from app.infra.celery_infra import celery_app
from app.routes.meal_prompt import generate_meal_plan_prompt


meal_router = APIRouter()


@meal_router.post("/meal-plans/")
async def create_meal_plan(person_login: str):
    try:
        person = Person.read(person_login)
        if person is None:
            raise HTTPException(status_code=404, detail="Person not found")
        prompt = generate_meal_plan_prompt(person)
        logger.info(prompt)
        task = celery_app.send_task("app.infra.celery_infra.generate_meal_plan", args=[person_login, prompt])
        return f"Meal plan task added to queue, task id: {task.id}"
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail="Error generating meal plan")


@meal_router.get("/meal-plans/{person_login}/status")
async def get_meal_plan_status(person_login: str):
    try:
        task_id = f"generate_meal_plan_{person_login}"
        task = celery_app.AsyncResult(task_id)
        if task.state == "SUCCESS":
            return {"status": "done"}
        elif task.state == "PENDING":
            return {"status": "pending"}
        else:
            return {"status": "error"}
    except Exception as e:
        logger(str(e))
        raise HTTPException(status_code=500, detail="Error getting meal plan status")


@meal_router.get("/meal-plans/{person_login}")
async def get_meal_plan(person_login: str):
    try:
        meal_plan = MealPlan.read(person_login)
        if meal_plan is None:
            raise HTTPException(status_code=404, detail="Meal plan not found")
        return meal_plan
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail="Error getting meal plan")

logger.debug("app.routes.meal file end reached")
