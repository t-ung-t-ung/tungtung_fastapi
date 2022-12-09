from fastapi import FastAPI
from routers import promise, user

from database.database import init_database
from routers import promise, user


init_database()

app = FastAPI()

app.include_router(promise.router)
app.include_router(user.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
