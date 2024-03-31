# external module imports
import uvicorn
import logging

# external package imports
from fastapi import FastAPI, APIRouter

# local imports
from src.routes.ball_machine import ball_machine

logger = logging.getLogger(__name__)
app = FastAPI(title="Fitness tracker API", openapi_url="/openapi.json")

api_router = APIRouter()
app.include_router(ball_machine.router, prefix="/ball-machine", tags=["ball_machine"])


@app.get("/", status_code=200)
def root():
    logger.info("home page ...")
    return {"message": "Hello World5"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8005, log_level="debug")
