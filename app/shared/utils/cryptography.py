from cryptography.fernet import Fernet
from app.config import get_env
import jwt

key = get_env('HASH_CRYPTOGRAPHY_KEY') 
fernet = Fernet(key) 

def encrypt(data: str) -> str:
    encrypted_bytes = fernet.encrypt(data.encode('utf-8'))
    return encrypted_bytes.decode('utf-8')

def decrypt(hash_str: str) -> str:
    decrypted_bytes = fernet.decrypt(hash_str.encode('utf-8'))
    return decrypted_bytes.decode('utf-8')

def encode(payload: any) -> str:
    return jwt.encode(
        payload,
        get_env('HASH_CRYPTOGRAPHY_KEY'),
        algorithm="HS256"
    )

def decode(payload: str) -> any:
    return jwt.decode(payload, get_env('HASH_CRYPTOGRAPHY_KEY'), algorithms=["HS256"])
