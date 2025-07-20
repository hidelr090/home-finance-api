from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

class TableCreateDTO(BaseModel):
  name: str
  
class TableUpdateDTO(BaseModel):
  name: Optional[str] = None

class TableDTO(TableCreateDTO):
  id: uuid4
  
  class Config:
    orm_mode = True