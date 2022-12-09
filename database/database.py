from sqlalchemy.future import Engine
from sqlmodel import create_engine, SQLModel, Session
from database import scheme_around

engine: Engine


def init_database():
    global engine

    engine = create_engine(
        f'mysql+pymysql://siun:tldjsWkd!123@127.0.0.1:3307/around',
        echo=False)

    SQLModel.metadata.create_all(engine)
    print("sdfsdffsd")




