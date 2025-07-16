from typing import Optional
from app.models.user import UserModel
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserUpdateDTO
from app.shared.utils.cryptography import encrypt
from app.shared.utils.exceptions import BusinessError, NotFoundError


class UpdateUserUseCase (): 
  def __init__(self, repo: UserRepository):
      self.repo = repo
  
  def execute(self, user_id: str, data: UserUpdateDTO) -> Optional[UserModel]:
      user_to_update = self.repo.get_by_id(user_id)

      if not user_to_update:
          raise NotFoundError(message="User not found")

      if data.password:
          if data.password != data.password_confirm:
              raise BusinessError("Passwords do not match")
          user_to_update.password_hash = encrypt(data.password)

      if data.email:
          user_to_update.email = data.email
          user_to_update.is_active = False

      update_data = data.model_dump(
          exclude_unset=True,
          exclude={"password", "password_confirm", "email"},
      )

      for field, value in update_data.items():
          setattr(user_to_update, field, value)

      self.repo.update(user_id, user_to_update.to_dict())
      return user_to_update
