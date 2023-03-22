from datetime import datetime

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    kakao_id: int = Field(unique=True)
    nickname: str
    image: str
    age: int | None = Field(nullable=False)
    gender: int | None = Field(nullable=False)
    introduction: str | None = Field(nullable=False)
    fcm_token: str | None = Field(nullable=False)


class Evaluation(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    evaluator: int = Field(foreign_key='user.id')
    evaluated_user: int = Field(foreign_key='user.id')
    promise_id: int = Field(foreign_key="promise.id")
    content: str
    star: int


class Promise(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner: int | None = Field(foreign_key="user.id", nullable=False)
    category_id: int | None = Field(foreign_key="category.id", nullable=False)
    title: str | None = Field(nullable=False)
    detail: str | None = Field(nullable=False)
    latitude: float | None = Field(nullable=False)
    longitude: float | None = Field(nullable=False)
    address: str | None = Field(nullable=False)
    start_time: datetime | None = Field(nullable=False)
    end_time: datetime | None = Field(nullable=False)
    image: str | None = Field(nullable=False)
    max_people: int | None = Field(nullable=False)
    status: int | None = Field(nullable=False)


class UserPromise(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='user.id')
    promise_id: int = Field(foreign_key='promise.id')
    is_auth: bool
    status: int | None = Field(nullable=False)
    start_time: datetime | None = Field(nullable=False)
    end_time: datetime | None = Field(nullable=False)


class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str


class Chat(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: int
    user_id: int = Field(foreign_key='user.id')
    promise_id: int = Field(foreign_key='promise.id')
    time: datetime = Field(default=datetime.now())
    content: str


class Notification(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    message: str
    type: int
    status: int
    time: datetime
    user_id: int = Field(foreign_key="user.id")
    promise_id: int | None = Field(foreign_key="promise.id")


class Banner(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    image: str
    link: str
