from fastapi import FastAPI
from multiprocessing import Process
from loguru import logger

from src.config import ENVIRONMENT
from src.solvers.solver import start_solver
from src.routes import status, subscription, user, puzzle

logger.info("ENVIRONMENT: {env}", env=ENVIRONMENT)

solver_process = Process(target=start_solver)
solver_process.start()

app = FastAPI()

app.include_router(status.router)
app.include_router(subscription.router)
app.include_router(user.router)
app.include_router(puzzle.router)

@app.get("/")
def read_root() -> dict:
    return {"Hello": "World"}

@app.get("/ping")
def ping() -> str:
    return "pong"

solver_process.join()
