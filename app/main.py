from fastapi import FastAPI
from fastapi import HTTPException
from app.routes.person import persons_router
from app.routes.meal import meal_router
from app.infra import startup
from app.infra.logger import logger


app = FastAPI()


# Register the startup event handler from the startup module
app.on_event("startup")(startup.startup_event)


# Register the routers
app.include_router(persons_router)
app.include_router(meal_router)

logger.debug("app.main file end reached")
