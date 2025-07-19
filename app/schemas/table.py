from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

class TableCreateDTO(BaseModel):
  name: str
  user_id: Optional[uuid4] = None
  
class TableUpdateDTO(BaseModel):
  name: Optional[str] = None
  user_id: Optional[uuid4] = None

class TableDTO(TableCreateDTO):
  id: uuid4
  
  class Config:
    orm_mode = True