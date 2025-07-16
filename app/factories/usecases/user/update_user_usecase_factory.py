from fastapi import Depends
from app.modules.user import UpdateUserUseCase
from app.factories.repositories.user_repository_factory import user_repository_factory
from app.repositories.user_repository import UserRepository
def update_user_usecase_factory(
  repo: UserRepository = Depends(user_repository_factory)
) -> UpdateUserUseCase:
  return UpdateUserUseCase(repo=repo)