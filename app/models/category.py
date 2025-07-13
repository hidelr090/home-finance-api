from sqlalchemy import Column, String, Float, ForeignKey
from app.models.base import BaseModelWithTimestamps
from sqlalchemy.orm import mapped_column, relationship

class CategoryModel(BaseModelWithTimestamps):
  __tablename__ = "category"

  name = Column(String, nullable= False)
  max_value = Column(Float, default=0)
  
  user_id = mapped_column(ForeignKey("user.id"))
  user = relationship("UserModel", back_populates="categories")