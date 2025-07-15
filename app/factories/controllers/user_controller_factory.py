from fastapi import Depends
from app.controllers.user_controller import UserController
from app.factories.usecases.user import create_user_usecase_factory

def user_controller_factory(
  create_user_usecase=Depends(create_user_usecase_factory)
) -> UserController:
  return UserController(create_user_usecase=create_user_usecase)
