from cryptography.fernet import Fernet
from app.config import get_env

key = get_env('HASH_CRYPTOGRAPHY_KEY') 
fernet = Fernet(key) 

def encrypt(data: str) -> str:
    encrypted_bytes = fernet.encrypt(data.encode('utf-8'))
    return encrypted_bytes.decode('utf-8')

def decrypt(hash_str: str) -> str:
    decrypted_bytes = fernet.decrypt(hash_str.encode('utf-8'))
    return decrypted_bytes.decode('utf-8')
