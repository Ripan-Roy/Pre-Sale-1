from fastapi import FastAPI
from tortoise import Tortoise, fields
from tortoise.models import Model
from auth.db_conenct import *
import asyncio

db = connect_db()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
