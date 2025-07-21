from app.models.category import CategoryModel
from app.models.table import TableModel
from app.models.user import UserModel
from app.repositories import TableRepository
from app.repositories.category_repository import CategoryRepository
from app.repositories.user_repository import UserRepository
from app.schemas.table import TableUpdateDTO
from app.shared.types.session import AuthSession
from app.shared.utils.exceptions import NotFoundError

class UpdateTableUseCase:
    def __init__(
        self,
        repo: TableRepository,
        category_repository: CategoryRepository,
        user_repository: UserRepository,
    ):
        self.__repo = repo
        self.__user_repository = user_repository
        self.__category_repository = category_repository

    def execute(self, session: AuthSession, table_id: str, data: TableUpdateDTO) -> TableModel:
        table = self.__repo.get_by_id(table_id)
        if not table:
            raise NotFoundError("Table not found")

        return self.__update_table(session, table_id, data)

    def __update_table(self, session: AuthSession, table_id: str, data: TableUpdateDTO) -> TableModel:
        table = self.__repo.get_by_id(table_id)
        if not table:
            raise NotFoundError("Table not found")
          
        user_ids = set(data.user_ids or [])
        existing_user_ids = {user.id for user in table.users}
        new_user_ids = user_ids - existing_user_ids

        category_ids = set(data.category_ids or [])
        existing_category_ids = {cat.id for cat in table.categories}
        new_category_ids = category_ids - existing_category_ids
        
        for user_id in new_user_ids:
          table.users.append(UserModel(id=user_id)) 

        for category_id in new_category_ids:
          table.categories.append(CategoryModel(id=category_id))

        users = self.__user_repository.list_by_ids(list(user_ids))
        categories = self.__category_repository.list_by_ids(data.category_ids or [])

        table.name = data.name
        table.updated_by = session["user"].id

        table.users = list(users)
        table.categories = list(categories)

        return self.__repo.update(table)