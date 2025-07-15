from cryptography.fernet import Fernet
from app.config import get_env

key = get_env('HASH_CRYPTOGRAPHY_KEY')
fernet = Fernet(key)
def encrypt(data: str) -> str:
  return fernet.encrypt(data.encode())

def decrypt(hash: str) -> str:
  return fernet.decrypt(hash)
