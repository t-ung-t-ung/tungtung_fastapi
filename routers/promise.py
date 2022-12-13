from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import func
from sqlmodel import Session, select
from database.scheme_around import Promise, User, UserPromise
from database.database import engine, getUser, getCategoryName, getUsersInPromise

router = APIRouter(
    prefix="/promise"
)

@router.get("/")
async def get_promises():
    result = []
    with Session(engine) as session:
        statement = select(Promise)
        promises = session.exec(statement).all()
        test = session.query(Promise.id, func.count(UserPromise.user_id)).join(UserPromise).filter(Promise.id == UserPromise.promise_id).group_by(UserPromise.promise_id).all()
        # 0인 애들 처리 해주기 이 방법은 너무 구려
        tmp = [0 for i in range(len(promises))]
        for t in test:
            tmp[t[0]-1] = t[1]
        for promise in promises:
            owner = getUser(promise.owner)
            category = getCategoryName(promise.category_id)
            result.append({"id": promise.id,
                           "owner": owner["nickname"],
                           "category": category,
                           "title": promise.title,
                           "detail": promise.detail,
                           "longitude": promise.longitude,
                           "latitude": promise.latitude,
                           "promise_time": promise.promise_time,
                           "image": promise.image,
                           "max_people": promise.max_people,
                           "current_people": tmp[promise.id-1]+1,
                           "status": promise.status})
        return result


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
