from fastapi import APIRouter, status
from sqlmodel import Session, select

from database.scheme_around import Category
from database.database import engine


router = APIRouter(
    prefix="/categories"
)


@router.get("/", response_model=list[Category], status_code=status.HTTP_200_OK)
async def get_all_category():
    with Session(engine) as session:
        statement = select(Category)
        categories = session.exec(statement).all()
        return categories
