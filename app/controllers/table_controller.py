from fastapi.params import Body
from app.modules.table.usecases.create import CreateTableUseCase
from app.modules.table.usecases.update import UpdateTableUseCase
from app.schemas.table import TableCreateDTO, TableUpdateDTO
from app.shared.types.session import AuthSession


class TableController:
  def __init__(
    self,
    create_table_usecase: CreateTableUseCase,
    update_table_usecase: UpdateTableUseCase
  ):
    self.__create_table_usecase = create_table_usecase,
    self.__update_table_usecase = update_table_usecase
    
  async def create_table(self, session: AuthSession,data: dict = Body(...)):
    data_dto = TableCreateDTO(**data)
    return self.__create_table_usecase.execute(session, data_dto)
  
  async def update_table(self, session: AuthSession, table_id:str, data: dict = Body(...)):
    data_dto = TableUpdateDTO(**data)
    return self.__update_table_usecase.execute(session, table_id, data_dto)