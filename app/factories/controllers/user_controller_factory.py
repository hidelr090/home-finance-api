from app.controllers.user_controller import UserController
from app.factories.usecases.user.create_user_usecase_factory import create_user_usecase_factory
def user_controller_factory():
  return UserController(
    create_user_usecase = create_user_usecase_factory()
  )