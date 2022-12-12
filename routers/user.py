from fastapi import APIRouter, Depends
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlmodel import Session, select

from database.database import engine
from database.scheme_around import User
from network.http_client import client

router = APIRouter(
    prefix="/user"
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")





@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"your user is": user_id}
