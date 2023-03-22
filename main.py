from fastapi import FastAPI
from database.database import init_database
from routers import promise, user, auth, category, chat

import firebase_admin
from firebase_admin import credentials

from firebase.send import send_message
from util import kakao_public_key

registration_token = 'fRd8eXP7RISDQZ4qHQCi_m:APA91bEoyZJo4qkMeK3Ti_jgPgmZnNJnU0fMAAEIJ2rR9rtSh9kXg_2bsA9p-REqby3vua49dj3PxDgesvrJjv4gKC6t8Kj3hN1et125muzrNtnwa6TKv2AK8yrEw36J4zVHJXizI0G1'

#
# cred = credentials.Certificate("firebase/hyu-around-firebase-adminsdk-hwbpd-acbbacf5a4.json")
# firebase_admin.initialize_app(cred)

app = FastAPI()

app.include_router(promise.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(category.router)
app.include_router(chat.router)


@app.on_event("startup")
async def on_startup():
    init_database()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    send_message(fcm_token=registration_token, title='title', body='body')
    return {"message": f"Hello {name}"}
