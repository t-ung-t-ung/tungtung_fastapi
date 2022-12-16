from fastapi import APIRouter, status
from sqlmodel import Session, select

from database.scheme_around import Category, CategoryCreate
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


@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
async def create_category(body: CategoryCreate):
    with Session(engine) as session:
        category = Category.from_orm(body)
        session.add(category)
        session.commit()
        session.refresh(category)
        return category
