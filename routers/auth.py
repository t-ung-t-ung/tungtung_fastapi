import base64
import json
import time
from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt, JOSEError
from pydantic import BaseModel
from sqlalchemy import select
from sqlmodel import Session

from database.scheme_around import User
from database.database import get_user, engine
from network.http_client import client
from util import kakao_public_key

router = APIRouter(
    prefix="/auth"
)

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


security = HTTPBearer()


async def has_kakao_access(credentials: HTTPAuthorizationCredentials = Depends(security)):
    def fix_padding(token):
        return token + "=" * (4 - len(token) % 4)

    async def verify_token(header, payload, signature):
        print(header, payload, signature, sep="\n")
        if payload["iss"] != "https://kauth.kakao.com":
            return False
        if payload["aud"] != "85fd169ddc2baf6b6237dbfbcbcc1e02":
            return False
        if payload["exp"] < time.time():
            return False
        if header["kid"] not in await kakao_public_key():
            return False
        print(jwt.decode(signature, header["kid"], "RS256"))
        return True

    print(credentials.credentials)
    tokens = credentials.credentials.split(".")

    if not await verify_token(json.loads(base64.b64decode(fix_padding(tokens[0])).decode()),
                              json.loads(base64.b64decode(fix_padding(tokens[1])).decode()),
                              tokens[2]):
        pass
    return f"hi"

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JOSEError as e:  # catches any exception
        raise HTTPException(
            status_code=401,
            detail=str(e))


@router.post("/signIn")
async def sign_in(token: str = Depends(has_kakao_access)):
    return token


@router.post("/login")
async def login():
    response = await client.get("https://kapi.kakao.com/v1/user/access_token_info",
                                headers={"Authorization": f"Bearer {login_body.kakao_id}"})
    kakao_id = response.json().get("id")
    if not kakao_id:
        raise HTTPException(
            status_code=401,
            detail="bad access token")
    with Session(engine) as session:
        user = session.exec(select(User).where(User.kakao_id == kakao_id)).one_or_none()
        if user:
            return {"access_token": create_access_token({"user_id": user.id})}
        else:
            return {"test": create_access_token({"user_id": 2})}


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(payload: dict = Depends(has_kakao_access)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = get_user(user_id=payload.get("user_id"))
    if user is None:
        raise credentials_exception
    return user


@router.get("/users", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
