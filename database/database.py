from sqlmodel import create_engine, SQLModel, Session, select

from database.scheme_around import User, Category

engine = create_engine(
    f'mysql+pymysql://siun:tldjsWkd!123@13.125.114.46:3306/around',
    echo=False)


def init_database():
    global engine

    SQLModel.metadata.create_all(engine)


def get_user(user_id: str):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).one_or_none()
        return user


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
