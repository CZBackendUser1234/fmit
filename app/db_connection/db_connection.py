from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.configs.configs import configs
from app.models.schemas import models

client = AsyncIOMotorClient(configs.MONGO_URI)


async def init_db():
    await init_beanie(database=client[configs.MONGO_DB_NAME], document_models=models)
