from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import UserModel
from app.shared.utils.exceptions import NotFoundError, RepositoryError

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
    
    def get_by_id(self, id: str) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.id == id).first()

    def list_all(self):
        return self.db.query(UserModel).all()
    
    def update(self, user_id: int, updates: dict) -> Optional[UserModel]:
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()

        if not db_user:
            raise NotFoundError(UserModel.__str__, user_id)

        for key, value in updates.items():
            if hasattr(db_user, key):
                setattr(db_user, key, value)
            else:
                raise RepositoryError()

        self.db.commit()

        self.db.refresh(db_user)
        return db_user
