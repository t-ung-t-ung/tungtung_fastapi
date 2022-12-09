from fastapi import FastAPI
from routers import promise, user

from database.database import init_database, engine
from routers import promise, user




app = FastAPI()

app.include_router(promise.router)
app.include_router(user.router)

@app.on_event("startup")
def on_startup():
    init_database()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
