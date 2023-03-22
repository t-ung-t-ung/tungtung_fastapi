from fastapi import APIRouter, status, Body, HTTPException
from sqlmodel import Session, select

from database.scheme_around import Chat
from database.database import engine


router = APIRouter(
    prefix="/chat"
)


@router.get("/", response_model=list[Chat], status_code=status.HTTP_200_OK, tags=['chat'])
async def get_all_chat():
    with Session(engine) as session:
        statement = select(Chat)
        chats = session.exec(statement).all()
        return chats


@router.post("/", response_model=Chat, status_code=status.HTTP_201_CREATED, tags=['chat'])
async def create_chat(chat: Chat = Body(
    example=Chat(
        type=0,
        user_id=1,
        promise_id=1,
        content="content"
    ).json(exclude_none=True)
)):
    with Session(engine) as session:
        session.add(chat)
        session.commit()
        session.refresh(chat)
        return chat
