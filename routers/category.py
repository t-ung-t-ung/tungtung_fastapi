from fastapi import APIRouter, status, Body, HTTPException
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


@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
async def create_category(category: Category = Body(
    example=Category(name="운동").json(exclude_none=True)
)):
    with Session(engine) as session:
        session.add(category)
        session.commit()
        session.refresh(category)
        return category


@router.patch("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def create_category(category_id: int, category: Category = Body(
    example=Category(name="운동").json(exclude_none=True)
)):
    with Session(engine) as session:
        db_category = session.get(Category, category_id)
        if not db_category:
            raise HTTPException(status_code=404, detail="Category not found")
        category_data = category.dict(exclude_unset=True)
        for key, value in category_data.items():
            setattr(db_category, key, value)
        session.add(db_category)
        session.commit()
        session.refresh(db_category)
