from fastapi import APIRouter, Response, status
from pydantic import BaseModel, constr

router = APIRouter(
    prefix="/puzzle",
    tags=["puzzle"],
    responses={status.HTTP_201_CREATED: {"description": "Puzzle created successfully."}}
)

PUZZLES = [
    "hashi",
    "maze-cover"
]

class Puzzle(BaseModel):
    name: str
    description: str
    puzzle: constr(regex="|".join(PUZZLES))

@router.post("/")
async def create_puzzle(puzzle: Puzzle) -> Response:
    return Response(status_code=status.HTTP_201_CREATED)
