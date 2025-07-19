from fastapi.params import Body
from app.modules.table.usecases.create import CreateTableUseCase
from app.schemas.table import TableCreateDTO
from app.shared.types.session import AuthSession


class TableController:
  
  def __init__(
    self,
    create_table_usecase: CreateTableUseCase,
  ):
    self.__create_table_usecase = create_table_usecase
    
  async def create_table(self, session: AuthSession,data: dict = Body(...)):
    data_dto = TableCreateDTO(**data)
    return self.__create_table_usecase.execute(session, data_dto)