from fastapi.params import Depends
from app.factories.repositories.table_repository_factory import table_repository_factory
from app.modules.table.usecases.create import CreateTableUseCase
from app.repositories.table_repository import TableRepository


def create_table_usecase_factory(
  repo: TableRepository = Depends(table_repository_factory)
) -> CreateTableUseCase:
  return CreateTableUseCase(repo = repo)