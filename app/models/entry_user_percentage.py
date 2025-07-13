from sqlalchemy import Column, Float, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from app.models.base import BaseModelWithTimestamps

class EntryUserPercentageModel(BaseModelWithTimestamps):
  __tablename__ = "entry_user_percentage"
  
  percentage = Column(Float, nullable=False)
  
  user_id = mapped_column(ForeignKey("user.id"))
  user = relationship("UserModel", back_populates="entry_user_percentages")
  
  entry_id = mapped_column(ForeignKey("entry.id"))
  entry = relationship("EntryModel", back_populates="entry_user_percentages")