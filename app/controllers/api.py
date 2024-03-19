from fastapi import APIRouter

from app.controllers.apis import weddings

api_router = APIRouter()
api_router.include_router(weddings.router, tags=["weddings"])
