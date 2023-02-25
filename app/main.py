from fastapi import FastAPI
from app.routes.person import persons_router
from app.infra import startup

app = FastAPI()

# Register the startup event handler from the startup module
app.on_event("startup")(startup.startup_event)

# Register the routers
app.include_router(persons_router)
