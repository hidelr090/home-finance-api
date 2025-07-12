from pydantic import BaseModel, EmailStr

class UserCreateDTO(BaseModel):
    name: str
    email: EmailStr

class UserDTO(UserCreateDTO):
    id: int

    class Config:
        orm_mode = True
