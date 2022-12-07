from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


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
