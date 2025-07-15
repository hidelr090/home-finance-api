from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import UserModel

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: UserModel) -> UserModel:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_email(self, email: str) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.email == email).first()

    def list_all(self):
        return self.db.query(UserModel).all()

