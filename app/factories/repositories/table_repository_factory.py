from fastapi import Depends
from app.infrastructure.database.connection import get_db
from app.repositories.table_repository import TableRepository
from sqlalchemy.orm import Session

def table_repository_factory(db: Session = Depends(get_db)) -> TableRepository:
  return TableRepository(db)