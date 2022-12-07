from datetime import datetime

from sqlmodel import Field, SQLModel

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

class Banner(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    image: str
    link: str

class Chat(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: int
    time: datetime
    content: str
    user_id: int = Field(foreign_key='user.id')
    promise_id: int = Field(foreign_key='promise.id')

class UserPromise(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='user.id')
    promise_id: int = Field(foreign_key='promise.id')
    is_auth: bool