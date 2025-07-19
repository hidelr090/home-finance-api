from app.models.table import TableModel
from app.repositories import TableRepository
from app.schemas.table import TableCreateDTO
from app.shared.types.session import AuthSession

class CreateTableUseCase():
  
  def __init__(self, repo: TableRepository):
    self.repo = repo
    
  def execute(self, session: AuthSession, data: TableCreateDTO) -> TableModel:
    print(session, 'sess')
    table = TableModel(
      name = data.name,
      user_id = session["user"].id
    )
    
    return self.repo.create(table)