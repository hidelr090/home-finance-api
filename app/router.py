from fastapi import APIRouter
from app.factories.controllers.user_controller_factory import user_controller_factory

api_router = APIRouter()

user_controller = user_controller_factory()

api_router.include_router(user_controller.router, prefix="/user", tags=["User"])

# uvicorn app.server:app --reload --host localhost --port 8080