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
    
class AuthUserDTO(BaseModel):
    email: str
    password: str
    
class UserUpdateDTO(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    password_confirm: Optional[str]
    is_active: Optional[bool]
    token: Optional[str]
    token_expiration: Optional[datetime]

class UserDTO(UserCreateDTO):
    id: uuid4

    class Config:
        orm_mode = True
        
