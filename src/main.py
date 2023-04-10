from fastapi import FastAPI

from src.routes import status, subscription, user, puzzle

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