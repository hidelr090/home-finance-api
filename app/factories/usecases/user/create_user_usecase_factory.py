from app.modules.user import CreateUserUseCase
from app.factories.repositories.user_repository_factory import user_repository_factory
def create_user_usecase_factory():
  return CreateUserUseCase(
    repo = user_repository_factory()
  )