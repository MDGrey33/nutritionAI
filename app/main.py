from fastapi import FastAPI
from app.routes.person import persons_router

app = FastAPI()

app.include_router(persons_router)
