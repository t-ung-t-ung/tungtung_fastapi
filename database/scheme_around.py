from datetime import datetime

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    kakao_id: int = Field(unique=True)
    nickname: str
    image: str


class Evaluation(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    evaluator: int = Field(foreign_key='user.id')
    evaluated_user: int = Field(foreign_key='user.id')
    promise_id: int = Field(foreign_key="promise.id")
    content: str
    star: int


class Promise(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner: int = Field(foreign_key="user.id")
    category_id: int = Field(foreign_key="category.id")
    title: str
    detail: str
    latitude: float
    longitude: float
    promise_time: datetime
    image: str
    max_people: int
    status: int


class UserPromise(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='user.id')
    promise_id: int = Field(foreign_key='promise.id')
    is_auth: bool


class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    image: str


class Chat(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: int
    user_id: int = Field(foreign_key='user.id')
    promise_id: int = Field(foreign_key='promise.id')
    time: datetime
    content: str


class Banner(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    image: str
    link: str
