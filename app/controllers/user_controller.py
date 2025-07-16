from app.modules.user.usecases.update import UpdateUserUseCase
from app.schemas.user import UserCreateDTO, AuthUserDTO, UserUpdateDTO
from ..modules.user import CreateUserUseCase, AuthUserUseCase
from fastapi.params import Body

class UserController:
    def __init__(
        self, 
        create_user_usecase: CreateUserUseCase,
        auth_user_usecase: AuthUserUseCase,
        update_user_usecase: UpdateUserUseCase
    ):
        self.__create_user_usecase = create_user_usecase
        self.__auth_user_usecase = auth_user_usecase
        self.__update_user_usecase = update_user_usecase

    async def list_users(self):
        return [{"id": 1, "name": "Fulano"}]

    async def create_user(self, data: dict = Body(...)):
        data_dto = UserCreateDTO(**data)
        return self.__create_user_usecase.execute(data_dto)
    
    async def authenticate(self, data: dict = Body(...)):
        data_dto = AuthUserDTO(**data)
        return self.__auth_user_usecase.execute(data_dto)
    
    async def update(self, user_id: str, data: UserUpdateDTO):
        data_dto = UserUpdateDTO(**data)
        return self.__update_user_usecase.execute(user_id, data_dto)
