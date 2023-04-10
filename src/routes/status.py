from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/status",
    tags=["status"],
)

class Status(BaseModel):
    id: int
    status: str


@router.get("/{id}")
async def get_status(id: int) -> Status:
    return  Status(id=id, status="OK")
