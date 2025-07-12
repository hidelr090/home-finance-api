from fastapi import APIRouter

class UserController:
    def __init__(self):
        self.router = APIRouter()
        self.router.get("/")(self.list_users)
        # outros endpoints aqui

    async def list_users(self):
        return [{"id": 1, "name": "Fulano"}]

user_controller = UserController()
