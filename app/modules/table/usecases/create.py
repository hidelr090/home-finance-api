from app.models.table import TableModel
from app.repositories import TableRepository
from app.repositories.category_repository import CategoryRepository
from app.repositories.user_repository import UserRepository
from app.schemas.table import TableCreateDTO
from app.shared.types.session import AuthSession

class CreateTableUseCase():
  
  def __init__(
    self, 
    repo: TableRepository,
    category_repository: CategoryRepository,
    user_repository: UserRepository
    ):
    self.__repo = repo
    self.__user_repository = user_repository
    self.__category_repository = category_repository
    
  def execute(self, session: AuthSession, data: TableCreateDTO) -> TableModel:
    user_ids = set(data.user_ids or [])
    user_ids.add(session["user"].id)
    
    users = self.__user_repository.list_by_ids(list(user_ids))
    unique_users = {user.id: user for user in users}.values()
    
    categories = self.__category_repository.list_by_ids(data.category_ids or [])
    unique_categories = {cat.id: cat for cat in categories}.values()
    
    table = TableModel(
        name=data.name,
        created_by=session["user"].id,
        updated_by=session["user"].id,
    )
    
    table.users.extend(unique_users)
    table.categories.extend(unique_categories)
    
    return self.__repo.create(table)

