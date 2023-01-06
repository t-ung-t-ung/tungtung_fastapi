from sqlmodel import create_engine, SQLModel, Session, select

from database.scheme_around import User, UserPromise, Notification

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


def get_participants(promise_id: int, session: Session):
    statement = select(User).join(UserPromise).where(UserPromise.promise_id == promise_id)
    users = session.exec(statement).all()
    return users


def create_notification(notification: Notification, session: Session):
    session.add(notification)
    session.commit()
