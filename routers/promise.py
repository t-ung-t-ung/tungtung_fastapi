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


class AllPromise(Promise, table=False):
    people: int


class Result(SQLModel):
    result: int


@router.get("/", response_model=list[AllPromise], status_code=status.HTTP_200_OK, tags=['Promise'])
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


@router.get("/search/", tags=['Promise'])
async def search_promises(sw_latitude: float, sw_longitude: float, ne_latitude: float, ne_longitude: float,
                          category_id: int | None = None):
    with Session(engine) as session:
        if category_id is not None:
            statement = select(Promise).where(Promise.latitude > sw_latitude, Promise.longitude > sw_longitude,
                                              Promise.latitude < ne_latitude, Promise.longitude < ne_longitude,
                                              Promise.category_id == category_id)
        else:
            statement = select(Promise).where(Promise.latitude > sw_latitude, Promise.longitude > sw_longitude,
                                              Promise.latitude < ne_latitude, Promise.longitude < ne_longitude)
        results = session.exec(statement).all()
        return results


@router.get("/{promise_id}", status_code=status.HTTP_200_OK, tags=['Promise'])
async def get_promise(promise_id: int):
    with Session(engine) as session:
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
            new_promise['owner_info'] = new_user
            new_promise['category_info'] = new_category
        participants = get_participants(new_promise['id'], session)
        new_promise['people'] = participants
        return new_promise


@router.post("/", response_model=Promise, status_code=status.HTTP_201_CREATED, tags=['Promise'])
async def create_promise(new_promise: Promise = Body(
    example=Promise(
        owner=1,
        category_id=1,
        title="제목",
        detail="자세한 내용",
        latitude=10.0,
        longitude=10.0,
        address="상세주소",
        start_time=datetime.now(),
        end_time=datetime.now(),
        image="image.img",
        max_people=5,
        status=0
    ).json(exclude_none=True)
)):
    with Session(engine) as session:
        session.add(new_promise)
        session.commit()
        session.refresh(new_promise)
        return new_promise


@router.post("/apply", tags=['Promise'])
async def apply_promise(user_promise: UserPromise = Body(
    example=UserPromise(
        user_id=1,
        promise_id=1,
        is_auth=0,
        start_time=datetime.now(),
        end_time=datetime.now()
    ).json()
)):
    user_promise.status = 2
    with Session(engine) as session:
        session.add(user_promise)
        session.commit()

        return {"result": 1}


@router.patch("/{promise_id}", response_model=Promise, status_code=status.HTTP_200_OK, tags=['Promise'])
async def update_promise(promise: Promise, promise_id: int):
    with Session(engine) as session:
        current_promise = session.get(Promise, promise_id)
        if not current_promise:
            raise HTTPException(status_code=404, detail="Promise not found")
        new_promise = promise.dict(exclude_unset=True)
        for key, value in new_promise.items():
            setattr(current_promise, key, value)
        session.add(current_promise)
        session.commit()
        session.refresh(current_promise)
        return current_promise


@router.patch("/apply/{option}", tags=['Promise'])
async def confirm_promise(user_id: int, promise_id: int, option: int):
    with Session(engine) as session:
        statement = select(UserPromise).where(UserPromise.promise_id == promise_id,
                                              UserPromise.user_id == user_id)
        current_user_promise = session.exec(statement).one()

        print(current_user_promise)

        if option == 1:
            setattr(current_user_promise, "status", 1)
        elif option == 0:
            setattr(current_user_promise, "status", 0)

        session.add(current_user_promise)
        session.commit()

        return {"result": 1}


@router.delete("/{promise_id}", response_model=Result, status_code=status.HTTP_200_OK, tags=['Promise'])
async def delete_promise(promise_id: int):
    with Session(engine) as session:
        promise = session.get(Promise, promise_id)

        if not promise:
            raise HTTPException(status_code=404, detail="Promise not found")

        setattr(promise, "status", -1)
        session.commit()

        return {"result": 1}
