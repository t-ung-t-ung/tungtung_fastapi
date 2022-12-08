from fastapi import APIRouter

router = APIRouter(
    prefix="/user"
)


@router.get("/")
async def get_users():
    return {"promises": 324}


@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"your user is": user_id}
