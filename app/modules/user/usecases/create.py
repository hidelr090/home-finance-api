from app.schemas.user import UserCreateDTO
from app.repositories.user_repository import UserRepository
from app.models.user import User

class CreateUserUseCase (): 
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, data: UserCreateDTO) -> User:
        existing = self.repo.get_by_email(data.email)
        if existing:
            raise ValueError("E-mail já cadastrado.")
        user = User(**data.model_dump())
        return self.repo.create(user)