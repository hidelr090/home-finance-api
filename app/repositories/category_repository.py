from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.category import CategoryModel

class CategoryRepository:
  
  def __init__(self, db: Session):
    self.db = db
    
  def create(self, category: CategoryModel) -> CategoryModel:
    self.db.flush() 
    self.db.expunge_all() 
    self.db.add(category)
    self.db.commit()
    self.db.refresh(category)
    return category
  
  def list_by_ids(self, ids: List[str]) -> Optional[List[CategoryModel]]:
    if not ids: return []
    return self.db.query(CategoryModel).filter(CategoryModel.id.in_(ids)).all()