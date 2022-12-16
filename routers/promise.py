import decimal

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import func
from sqlmodel import Session, select, func
from database.scheme_around import Promise, User, UserPromise, Category
from database.database import engine, get_participants

router = APIRouter(
    prefix="/promise"
)


@router.get("/")
async def get_promises():
    with Session(engine) as session:
        output = []

        statement = select(Promise, func.count(UserPromise.id)).join(UserPromise, isouter=True).group_by(Promise.id)
        results = session.exec(statement)
        for promise, user_number in results:
            if user_number:
                user_number = int(user_number)
            else:
                user_number = 0
            new_promise: dict = promise.dict()
            new_promise["people"] = user_number
            output.append(new_promise)
        return output


@router.get("/{promise_id}")
async def get_promise(promise_id: int):
    with Session(engine) as session:
        print(type(session))
        statement = select(Promise, User, Category).join(User, isouter=False).join(Category, isouter=True).where(Promise.id == promise_id)
        result = session.exec(statement)
        for promise, user, category in result:
            new_promise: dict = promise.dict()
            del(new_promise['owner'])
            del(new_promise['category_id'])
            new_user: dict = user.dict()
            del(new_user['kakao_id'])
            new_category: dict = category.dict()
            print(new_category)
            new_promise['owner'] = new_user
            new_promise['category'] = new_category
        participants = get_participants(new_promise['id'], session)
        new_promise['people'] = participants
        return new_promise

# @router.post("/")
# async def post_promise(newPromise: Promise):
#     with Session(engine) as session:
#         session.add(newPromise)
#         session.commit()
#         return {"result": 1}
