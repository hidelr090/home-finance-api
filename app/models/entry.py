from typing import List
from sqlalchemy import Integer, Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from ..models import BaseModelWithTimestamps, EntryUserPercentageModel
from datetime import datetime as dt

class EntryModel(BaseModelWithTimestamps):
  __tablename__ = "entry"
  
  description = Column(String, nullable=True, default='')
  amount = Column(Float, nullable=False, default=0)
  date = Column(DateTime, nullable=False, default=dt.now)
  entry_type = Column(Integer, nullable=False)
  
  entry_user_percentages: Mapped[List["EntryUserPercentageModel"]] = relationship(back_populates="entry")
  
  user_id = mapped_column(ForeignKey("user.id"))
  user = relationship("UserModel", back_populates="entries")
  
  table_id = mapped_column(ForeignKey("table.id"))
  table = relationship("TableModel", back_populates="entries")
  
  category_id = mapped_column(ForeignKey("category.id"))
  category = relationship("CategoryModel", back_populates="entries")