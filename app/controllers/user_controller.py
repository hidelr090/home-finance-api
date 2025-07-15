from app.schemas.user import UserCreateDTO
from ..modules.user import CreateUserUseCase
from fastapi.params import Body

class UserController:
    def __init__(self, create_user_usecase: CreateUserUseCase):
        self.create_user_usecase = create_user_usecase

    async def list_users(self):
        return [{"id": 1, "name": "Fulano"}]

    async def create_user(self, data: dict = Body(...)):
        data_dto = UserCreateDTO(**data)
        return self.create_user_usecase.execute(data_dto)
