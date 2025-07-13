from sqlalchemy.orm import Session
from fastapi import Depends
from ...infrastructure import get_db
from ...repositories.user_repository import UserRepository

def user_repository_factory(db: Session = Depends(get_db)) -> UserRepository:
  return UserRepository(db)