from fastapi import FastAPI
from database.database import init_database
from routers import promise, user, auth, category

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("firebase/hyu-around-firebase-adminsdk-hwbpd-acbbacf5a4.json")
firebase_admin.initialize_app(cred)

app = FastAPI()

app.include_router(promise.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(category.router)

@app.on_event("startup")
def on_startup():
    init_database()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
