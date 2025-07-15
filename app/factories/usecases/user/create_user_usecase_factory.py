from fastapi import Depends
from app.modules.user import CreateUserUseCase
from app.factories.repositories.user_repository_factory import user_repository_factory
from app.repositories.user_repository import UserRepository
def create_user_usecase_factory(
  repo: UserRepository = Depends(user_repository_factory)
) -> CreateUserUseCase:
  return CreateUserUseCase(repo=repo)