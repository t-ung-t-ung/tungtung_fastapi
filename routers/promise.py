from fastapi import APIRouter
from sqlmodel import Session, select
from database.scheme_around import Promise
from database.database import engine, getUserNickname, getCategoryName

router = APIRouter(
    prefix="/promise"
)


# @router.get("/")
# async def get_promises():
#     with Session(engine) as session:
#         statement = select(Promise)
#         results = session.exec(statement)
#         for promise in results:
            # json 배열에 넣기



@router.get("/{promise_id}")
async def get_promise(promise_id: int):
    with Session(engine) as session:
        statement = select(Promise).where(Promise.id == promise_id)
        promise = session.exec(statement).one_or_none()
        owner = getUserNickname(promise.owner)
        category = getCategoryName(promise.category_id)
        return {"id": promise.id,
                "owner": owner,
                "category": category,
                "title": promise.title,
                "detail": promise.detail,
                "longitude": promise.longitude,
                "latitude": promise.latitude,
                "datetime": promise.promise_time,
                "status": promise.status}
