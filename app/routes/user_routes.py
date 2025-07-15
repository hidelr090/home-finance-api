from fastapi import APIRouter, Depends
from app.factories.controllers.user_controller_factory import user_controller_factory
from app.controllers.user_controller import UserController
from fastapi.params import Body

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/")
async def list_users(controller: UserController = Depends(user_controller_factory)):
    return await controller.list_users()

@router.post("/")
async def create_user(data: dict = Body(...), controller: UserController = Depends(user_controller_factory)):
    return await controller.create_user(data)
