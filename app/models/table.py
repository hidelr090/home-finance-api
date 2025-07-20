from typing import List
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped

from app.models.associations.table_category import TableCategoryModel
from app.models.associations.user_table import UserTableModel
from app.models.base import BaseModelWithTimestamps
from app.models.entry import EntryModel

class TableModel(BaseModelWithTimestamps):
  __tablename__ = "table"
  
  name = Column(String, nullable=False, default='')
  
  user_id = mapped_column(ForeignKey("user.id"))
  user = relationship("UserModel", back_populates="tables")
  
  entries: Mapped[List["EntryModel"]] = relationship(back_populates="table")
  categories = relationship("CategoryModel", secondary = UserTableModel)
  users = relationship("UserModel", secondary = TableCategoryModel, back_populates = "user")