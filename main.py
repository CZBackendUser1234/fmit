from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.configs.configs import configs
from app.controllers.api import api_router
from app.db_connection import db_connection

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await db_connection.init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router, prefix=configs.API_V1_STR)

@app.get("/health")
async def root():
    return {"status": "OK"}