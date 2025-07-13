from dotenv import load_dotenv
import os

def setup_env():
  load_dotenv()

def get_env(env_var: str):
  os.getenv(env_var)