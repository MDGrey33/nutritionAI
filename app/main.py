from fastapi import FastAPI
from app.routes.person import router as person_router
from app.infra import logger

app = FastAPI()


# Mount the person router
app.include_router(person_router)
logger.logger.debug('person routes called')


# Test route to ensure everything is working
@app.get("/")
async def read_root():
    return {"Hello": "World"}

logger.logger.debug('reached end of file')
