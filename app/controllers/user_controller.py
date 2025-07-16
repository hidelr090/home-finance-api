from app.schemas.user import UserCreateDTO, AuthUserDTO
from ..modules.user import CreateUserUseCase, AuthUserUseCase
from fastapi.params import Body

class UserController:
    def __init__(
        self, 
        create_user_usecase: CreateUserUseCase,
        auth_user_usecase: AuthUserUseCase
    ):
        self.__create_user_usecase = create_user_usecase
        self.__auth_user_usecase = auth_user_usecase

    async def list_users(self):
        return [{"id": 1, "name": "Fulano"}]

    async def create_user(self, data: dict = Body(...)):
        data_dto = UserCreateDTO(**data)
        return self.__create_user_usecase.execute(data_dto)
    
    async def authenticate(self, data: dict = Body(...)):
        data_dto = AuthUserDTO(**data)
        return self.__auth_user_usecase.execute(data_dto)
