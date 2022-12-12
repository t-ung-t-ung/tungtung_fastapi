from fastapi import FastAPI

from database.database import init_database
from routers import promise, user, auth

app = FastAPI()

app.include_router(promise.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.on_event("startup")
def on_startup():
    init_database()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/webhook")
async def webhook(anything: dict | None = None):
    print(anything, "some")
    return {}
