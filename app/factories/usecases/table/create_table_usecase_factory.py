from fastapi.params import Depends
from app.factories.repositories import category_repository_factory, user_repository_factory
from app.factories.repositories.table_repository_factory import table_repository_factory
from app.modules.table.usecases.create import CreateTableUseCase
from app.repositories.category_repository import CategoryRepository
from app.repositories.table_repository import TableRepository
from app.repositories.user_repository import UserRepository


def create_table_usecase_factory(
  repo: TableRepository = Depends(table_repository_factory),
  category_repository: CategoryRepository = Depends(category_repository_factory),
  user_repository: UserRepository = Depends(user_repository_factory)
) -> CreateTableUseCase:
  return CreateTableUseCase(
    repo = repo,
    category_repository = category_repository,
    user_repository = user_repository
    )