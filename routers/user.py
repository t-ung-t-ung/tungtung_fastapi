from fastapi import APIRouter
from sqlalchemy.future import Engine

router = APIRouter(
    prefix="/user"
)

engine: Engine


@router.get("/")
async def get_users():
    return {"promises": 324}


@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"your user is": user_id}
