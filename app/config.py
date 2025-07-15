from dotenv import load_dotenv
import os

load_dotenv()

def get_env(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise RuntimeError(f"Variável {key} não encontrada.")
    return value
