from fastapi import APIRouter, Response
from pydantic import BaseModel

router = APIRouter(
    prefix="/puzzle",
    tags=["puzzle"],
)

class Puzzle(BaseModel):
    name: str
    description: str
    puzzle: str

@router.post("/")
async def create_puzzle(puzzle: Puzzle) -> Response:
    return Response(status_code=201)
