from sqlalchemy.future import Engine
from sqlmodel import create_engine, SQLModel, Session
from database import scheme_around
from database.scheme_around import User


engine = create_engine(
    f'mysql+pymysql://siun:tldjsWkd!123@13.125.114.46:3306/around',
    echo=False)


def init_database():
    global engine

    SQLModel.metadata.create_all(engine)


def get_user_by_kakao_id(kakao_id: str):
    with Session(engine) as session:
        statement = select(User).where(User.kakao_id == kakao_id)
        user = session.exec(statement).one_or_none()
        return user

