from app.schemas.user import UserCreateDTO
from app.repositories.user_repository import UserRepository
from app.models.user import UserModel
from app.shared.utils.cryptography import encrypt
from app.shared.utils.exceptions import BusinessError

class CreateUserUseCase (): 
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, data: UserCreateDTO) -> UserModel:
        existing = self.repo.get_by_email(data.email)
        if existing:
            raise BusinessError("E-mail já cadastrado.")
        
        if data.password_confirm != data.password:
            raise BusinessError("Senhas nao conferem")

        user = UserModel(
            name=data.name,
            surname=data.surname,
            email=data.email,
            password_hash=encrypt(data.password),
            is_active=data.is_active,
            token=data.token,
            token_expiration=data.token_expiration
        )

        return self.repo.create(user)