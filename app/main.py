from fastapi import FastAPI
from fastapi import HTTPException
from app.routes.person import persons_router
from app.infra import startup
from app.infra.error_handler import http_exception_handler
from app.infra.error_handler import generic_exception_handler

app = FastAPI()

# Register the error handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)


# Register the startup event handler from the startup module
app.on_event("startup")(startup.startup_event)


# Register the routers
app.include_router(persons_router)
