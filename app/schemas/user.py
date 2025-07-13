from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from uuid import uuid4

class UserCreateDTO(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password_hash: str
    is_active: bool
    token: Optional[str] = None
    token_expiration: Optional[datetime] = None
    

class UserDTO(UserCreateDTO):
    id: uuid4

    class Config:
        orm_mode = True
