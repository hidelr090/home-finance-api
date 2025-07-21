from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

class TableCreateDTO(BaseModel):
  name: str
  user_ids: Optional[List[str]] = []
  category_ids: Optional[List[str]] = []
  
class TableUpdateDTO(BaseModel):
  name: Optional[str] = None
  user_ids: Optional[List[str]] = []
  category_ids: Optional[List[str]] = []
class TableDTO(TableCreateDTO):
  id: uuid4
  
  class Config:
    orm_mode = True