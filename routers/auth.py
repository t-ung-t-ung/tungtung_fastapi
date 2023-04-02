import base64
import json
import time
from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt, JOSEError, ExpiredSignatureError
from jose.exceptions import JWTClaimsError
from pydantic import BaseModel
from sqlalchemy import select
from sqlmodel import Session
from starlette.responses import JSONResponse

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


async def verify_token(header, payload, credential):
    if payload["iss"] != "https://kauth.kakao.com":
        return False
    if payload["aud"] != "85fd169ddc2baf6b6237dbfbcbcc1e02":
        return False
    if payload["exp"] < time.time():
        return False
    keys = await kakao_public_key()
    for key in keys["keys"]:
        if key["kid"] == header["kid"]:
            try:
                jwt.decode(credential, key, "RS256", audience=payload["aud"])
            except (JWTError, ExpiredSignatureError, JWTClaimsError) as e:
                raise HTTPException(
                    status_code=401,
                    detail=str(e))
            return True
    return False


def fix_padding(token):
    return token + "=" * (4 - len(token) % 4)


async def has_kakao_access(credentials: HTTPAuthorizationCredentials = Depends(security)):
    credential = credentials.credentials
    tokens = credential.split(".")
    header = json.loads(base64.b64decode(fix_padding(tokens[0])).decode())
    payload = json.loads(base64.b64decode(fix_padding(tokens[1])).decode())

    if await verify_token(header, payload, credential):
        return payload
    return None


async def get_kakao_id(token: dict | None = Depends(has_kakao_access)):
    if token is None:
        return None
    return token["sub"]


@router.post("/signIn", tags=["Auth"],
             responses={
                 404: {"description": "카카오 아이디에 해당하는 유저가 없기 때문에 회원가입을 해야 합니다.",
                       "content": {
                           "application/json": {
                               "example": {"message": "No matching user."}
                           }
                       }},
                 200: {
                     "description": "앱을 사용하기 위한 액세스 토큰 발급.",
                     "content": {
                         "application/json": {
                             "example": {"access_token": "{access_token}"}
                         }
                     },
                 },
             })
def sign_in(kakao_id: str | None = Depends(get_kakao_id)):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.kakao_id == kakao_id)).one_or_none()
        if user:
            return {"access_token": create_access_token({"access_token": user.id})}
        else:
            return JSONResponse(status_code=404, content={"message": "No matching user."})


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
