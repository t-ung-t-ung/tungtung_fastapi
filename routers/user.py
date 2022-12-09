from fastapi import APIRouter, Depends

from sqlmodel import select, Session, create_engine

from database.database import engine
from database.scheme_around import User

router = APIRouter(
    prefix="/user"
)


@router.get("/")
async def get_users():
    with Session(engine) as session:
        user = session.exec(select(User)).one_or_none()

    return {"promises": user.nickname}


@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"your user is": user_id}
