from sqlalchemy.future import Engine
from sqlmodel import create_engine, SQLModel, Session, select
from database import scheme_around
from database.scheme_around import User


engine: Engine


def init_database():
    global engine

    engine = create_engine(
        f'mysql+pymysql://siun:tldjsWkd!123@13.125.114.46:3306/around',
        echo=False)

    SQLModel.metadata.create_all(engine)
    print("sdfsdffsd")


def get_user_by_kakao_id(kakao_id: str):
    with Session(engine) as session:
        statement = select(User).where(User.kakao_id == kakao_id)
        user = session.exec(statement).one_or_none()
        return user

