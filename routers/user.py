from fastapi import APIRouter
from passlib.context import CryptContext
from sqlmodel import Session, select

from database.database import engine
from database.scheme_around import Notification

router = APIRouter(
    prefix="/user"
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"your user is": user_id}


@router.get("/{user_id}/notifications", response_model=list[Notification])
async def get_all_notification(user_id: int):
    with Session(engine) as session:
        statement = select(Notification).where(Notification.user_id == user_id)
        notifications = session.exec(statement).all()
        return notifications
