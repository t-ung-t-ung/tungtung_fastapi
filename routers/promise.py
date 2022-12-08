from fastapi import APIRouter

router = APIRouter(
    prefix="/promise"
)


@router.get("/")
async def get_promises():
    return {"promises": 324}


@router.get("/{promise_id}")
async def get_promise(promise_id: int):
    return {"your promise is": promise_id}
