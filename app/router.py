from fastapi import APIRouter
from app.controllers.user_controller import user_controller

api_router = APIRouter()

api_router.include_router(user_controller.router, prefix="/user", tags=["User"])

# uvicorn app.server:app --reload --host localhost --port 8080