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


class LoginBody(BaseModel):
    kakao_id: str = "RF_AT0nSsXu-_f0j31rB03uDrLN7B2uw8bQeiRbzCisM1AAAAYT20yp7"


@router.get("/login")
async def login(login_body: LoginBody = LoginBody()):
    response = await client.get("https://kapi.kakao.com/v1/user/access_token_info",
                                headers={"Authorization": f"Bearer {login_body.kakao_id}"})
    kakao_id = response.json()["id"]
    with Session(engine) as session:
        user = session.exec(select(User).where(User.kakao_id == kakao_id)).one_or_none()
        if user:
            return {"access_token": user.id}
        else:
            return {}


@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"your user is": user_id}
