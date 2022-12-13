from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import Engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine, SQLModel, Session, select
from database import scheme_around
from database.scheme_around import User, Category, UserPromise

engine = create_engine(
    f'mysql+pymysql://siun:tldjsWkd!123@13.125.114.46:3306/around',
    echo=False)


def init_database():
    global engine

    SQLModel.metadata.create_all(engine)

def getUserNickname(user_id: int):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).one_or_none()
        return user.nickname

def getCategoryName(category_id: int):
    with Session(engine) as session:
        statement = select(Category).where(Category.id == category_id)
        category = session.exec(statement).one_or_none()
        return category.name

def getUsersInPromise(promise_id: int):
    with Session(engine) as session:
        statement = select(User).join(UserPromise).where(UserPromise.promise_id == promise_id)
        users = session.exec(statement).all()
        return users
