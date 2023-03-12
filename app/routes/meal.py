"""app.routes.meal"""
from fastapi import APIRouter, HTTPException
from app.models.meal import MealPlan
from app.models.person import Person
from app.infra.logger import logger
from app.infra.celery_infra import celery_app


meal_router = APIRouter()


@meal_router.post("/meal-plans/")
async def create_meal_plan(person_login: str):
    try:
        person = Person.read(person_login)
        if person is None:
            raise HTTPException(status_code=404, detail="Person not found")
        task = celery_app.send_task("app.infra.celery_infra.generate_meal_plan", args=[person_login])
        return f"Meal plan task added to queue, task id: {task.id}"
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail="Error generating meal plan")


logger.debug("app.routes.meal file end reached")
