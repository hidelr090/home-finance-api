from fastapi import Depends
from app.infrastructure.database.connection import get_db
from app.repositories.category_repository import CategoryRepository
from sqlalchemy.orm import Session

def category_repository_factory(db: Session = Depends(get_db)) -> CategoryRepository:
  return CategoryRepository(db)