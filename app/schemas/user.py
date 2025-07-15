from pydantic import EmailStr, BaseModel
from datetime import datetime
from typing import Optional
from uuid import uuid4

class UserCreateDTO(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str
    password_confirm: str
    is_active: bool = False
    token: Optional[str] = None
    token_expiration: Optional[datetime] = None
    

class UserDTO(UserCreateDTO):
    id: uuid4

    class Config:
        orm_mode = True
