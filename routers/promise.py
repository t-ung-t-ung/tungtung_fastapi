from datetime import datetime

from fastapi import APIRouter, status, Body, HTTPException
from sqlmodel import Session, select, func, SQLModel
from database.scheme_around import Promise, User, UserPromise, Category
from database.database import engine, get_participants

router = APIRouter(
    prefix="/promise"
)


class UserResponse(SQLModel):
    id: int
    nickname: str
    image: str


class Result(SQLModel):
    result: int


@router.get("/", status_code=status.HTTP_200_OK)
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


@router.get("/{promise_id}", status_code=status.HTTP_200_OK)
async def get_promise(promise_id: int):
    with Session(engine) as session:
        print(type(session))
        statement = select(Promise, User, Category).join(User, isouter=False).join(Category, isouter=True).where(
            Promise.id == promise_id)
        result = session.exec(statement)
        for promise, user, category in result:
            new_promise: dict = promise.dict()
            del (new_promise['owner'])
            del (new_promise['category_id'])
            new_user: dict = user.dict()
            del (new_user['kakao_id'])
            new_category: dict = category.dict()
            print(new_category)
            new_promise['owner'] = new_user
            new_promise['category'] = new_category
        participants = get_participants(new_promise['id'], session)
        new_promise['people'] = participants
        return new_promise


@router.post("/", response_model=Promise, status_code=status.HTTP_201_CREATED)
async def create_promise(new_promise: Promise = Body(
    example=Promise(
        owner=1,
        category_id=1,
        title="제목",
        detail="자세한 내용",
        latitude=10.0,
        longitude=10.0,
        promise_time="2000-00-00T00:00:00",
        image="image.img",
        max_people=5,
        status=0
    ).json()
)):
    with Session(engine) as session:
        session.add(new_promise)
        session.commit()
        session.refresh(new_promise)
        return new_promise


@router.patch("/", response_model=Promise, status_code=status.HTTP_200_OK)
async def update_promise(promise: Promise):
    if not promise.id:
        raise HTTPException(status_code=400, detail="Promise id not found")
    with Session(engine) as session:
        current_promise = session.get(Promise, promise.id)
        if not current_promise:
            raise HTTPException(status_code=404, detail="Promise not found")
        new_promise = promise.dict(exclude_unset=True)
        for key, value in new_promise.items():
            setattr(current_promise, key, value)
        session.add(current_promise)
        session.commit()
        session.refresh(current_promise)
        return current_promise


@router.delete("/{promise_id}", response_model=Result, status_code=status.HTTP_200_OK)
async def delete_promise(promise_id: int):
    with Session(engine) as session:
        promise = session.get(Promise, promise_id)
        user_promises = session.exec(select(UserPromise).where(UserPromise.promise_id == promise_id)).all()

        if not promise:
            raise HTTPException(status_code=404, detail="Promise not found")

        for user_promise in user_promises:
            session.delete(user_promise)
            session.commit()

        session.delete(promise)
        session.commit()

        return {"result": 1}
