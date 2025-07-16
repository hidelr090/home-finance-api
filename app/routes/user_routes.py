from fastapi import APIRouter, Depends
from app.factories.controllers.user_controller_factory import user_controller_factory
from app.controllers.user_controller import UserController
from fastapi.params import Body
from app.schemas.user import UserUpdateDTO
from app.shared.middlewares.auth import auth_middleware

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/")
async def list_users(
    _: None = Depends(auth_middleware),
    controller: UserController = Depends(user_controller_factory)
):
    return await controller.list_users()

@router.post("/")
async def create_user(data: dict = Body(...), controller: UserController = Depends(user_controller_factory)):
    return await controller.create_user(data)

@router.put("/{user_id}")
async def update_user(
    user_id: str,
    data: dict = Body(...),
    _: None = Depends(auth_middleware),
    controller: UserController = Depends(user_controller_factory),
):
    return await controller.update(user_id, data)

@router.post("/auth")
async def auth_user(data: dict = Body(...), controller: UserController = Depends(user_controller_factory)):
    return await controller.authenticate(data)