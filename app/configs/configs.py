import os

from pydantic_settings import BaseSettings

env_file_path = os.getenv("ENV_FILE_PATH", default="fmit.prod.env")


class Configs(BaseSettings):
    ENVIRONMENT: str
    API_V1_STR: str = "/api/v1"
    # MongoDB configuration
    MONGO_URI: str
    MONGO_DB_NAME: str

    class Config:
        extra = "allow"
        env_file = env_file_path
        env_file_encoding = 'utf-8'


configs = Configs()
