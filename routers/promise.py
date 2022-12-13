import decimal

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import func
from sqlmodel import Session, select, func
from database.scheme_around import Promise, User, UserPromise
from database.database import engine, getUser, getCategoryName, getUsersInPromise

router = APIRouter(
    prefix="/promise"
)


@router.get("/")
async def get_promises():
    with Session(engine) as session:
        output = []

        statement = select(Promise, func.sum(UserPromise.id)).join(UserPromise, isouter=True).group_by(Promise.id)
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
        statement = select(Promise).where(Promise.id == promise_id)
        promise = session.exec(statement).one_or_none()
        owner = getUser(promise.owner)
        category = getCategoryName(promise.category_id)
        participants = getUsersInPromise(promise.id)
        return {"id": promise.id,
                "owner": owner,
                "category": category,
                "title": promise.title,
                "detail": promise.detail,
                "longitude": promise.longitude,
                "latitude": promise.latitude,
                "promise_time": promise.promise_time,
                "image": promise.image,
                "max_people": promise.max_people,
                "current_people": participants,
                "status": promise.status}

# @router.post("/")
# async def post_promise(newPromise: Promise):
#     with Session(engine) as session:
#         session.add(newPromise)
#         session.commit()
#         return {"result": 1}
