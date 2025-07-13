from fastapi import APIRouter
from fastapi.params import Body
from ..modules.user import CreateUserUseCase

class UserController:
    def __init__(
        self,
        create_user_usecase: CreateUserUseCase
    ):
        self.router = APIRouter()
        
        self.router.get("/")(self.list_users, dependencies = [])
        self.router.post("/")(self.create_user)
        
        self.create_user_usecase = create_user_usecase

    async def list_users(self):
        return [{"id": 1, "name": "Fulano"}]
    
    async def create_user(self, data: dict = Body(...)):
        return self.create_user_usecase.execute(data)
