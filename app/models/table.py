from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from app.models.base import BaseModelWithTimestamps

class TableModel(BaseModelWithTimestamps):
  __tablename__ = "table"
  
  name = Column(String, nullable=False, default='')
  
  user_id = mapped_column(ForeignKey("user.id"))
  user = relationship("UserModel", back_populates="tables")