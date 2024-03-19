from fastapi import FastAPI

from app.configs.configs import configs
from app.controllers.api import api_router
from app.db_connection import db_connection

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await db_connection.init_db()

app.include_router(api_router, prefix=configs.API_V1_STR)


@app.get("/health")
async def root():
    return {"status": "OK"}
