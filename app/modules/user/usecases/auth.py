from app.repositories.user_repository import UserRepository
from datetime import datetime, timezone, timedelta
from app.schemas.user import AuthUserDTO
from app.shared.utils.cryptography import encode
from app.shared.utils.exceptions import AuthenticationError, BusinessError

class AuthUserUseCase (): 
  def __init__(self, repo: UserRepository):
      self.repo = repo
  
  def execute(self, data: AuthUserDTO) -> dict:
    if not data.email or not data.password:
      raise AuthenticationError("Credentials not provided")
  
    user = self.repo.get_by_email(data.email)
    
    if not user:
      raise BusinessError("Entity not found")

    encode_payload = {"id": user.id, "exp": datetime.now(timezone.utc) + timedelta(minutes=30)}
    
    token = encode(encode_payload)
    refresh_token = encode({"token": token})
    
    self.repo.update(user.id, { "token": token, "token_expiration": encode_payload["exp"] })

    return {
      "token": token,
      "refresh_token": refresh_token
    }

  