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