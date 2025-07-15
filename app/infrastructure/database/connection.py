from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_CONNECTION_URL')
print(DATABASE_URL)

engine = create_engine(DATABASE_URL) 
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False)

Base = declarative_base()

import app.models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
