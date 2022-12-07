from datetime import datetime

from sqlmodel import Field, SQLModel


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

