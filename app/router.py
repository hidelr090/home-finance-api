from fastapi import APIRouter

from app.routes import user_router
from app.routes import table_router

api_router = APIRouter()

api_router.include_router(user_router)
api_router.include_router(table_router)

# uvicorn app.server:app --reload --host localhost --port 8080