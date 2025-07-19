from fastapi.params import Depends
from app.controllers.table_controller import TableController
from app.factories.usecases.table.create_table_usecase_factory import create_table_usecase_factory


def table_controller_factory(
  create_table_usecase = Depends(create_table_usecase_factory)
) -> TableController:
  return TableController(
    create_table_usecase = create_table_usecase
  )