from typing import Optional
from sqlalchemy.orm import Session

from app.models.table import TableModel

class TableRepository:
  
  def __init__(self, db: Session):
    self.db = db
    
  def create(self, table: TableModel) -> TableModel:
    self.db.add(table)
    self.db.commit()
    self.db.refresh(table)
    return table
  
  def update(self, table: TableModel) -> TableModel:
    updated = self.db.merge(table)
    self.db.commit()
    self.db.refresh(updated)
    return updated

  def get_by_id(self, id: str) -> Optional[TableModel]:
    return self.db.query(TableModel).filter(TableModel.id == id).first()
