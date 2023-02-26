from fastapi import HTTPException, FastAPI
from fastapi.responses import JSONResponse
from app.infra import logger
log = logger.logger

app = FastAPI()


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    log.debug(f"HTTPException occurred: {exc}")
    return JSONResponse(content={"error": exc.detail}, status_code=exc.status_code)


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    log.debug(f"Unexpected exception occurred: {exc}")
    return JSONResponse(content={"error": "An unexpected error occurred"}, status_code=500)
