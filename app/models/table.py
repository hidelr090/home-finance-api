from __future__ import annotations

from typing import List, TYPE_CHECKING
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped

from app.models.associations import user_table
from app.models.associations import table_category
from app.models.associations.table_category import table_category
from app.models.associations.user_table import user_table
from app.models.base import BaseModelWithTimestamps
from app.models.entry import EntryModel

if TYPE_CHECKING:
    from app.models.user import UserModel

class TableModel(BaseModelWithTimestamps):
  __tablename__ = "table"
  
  name = Column(String, nullable=False, default='')
  
  user_id = mapped_column(ForeignKey("user.id"))
  user = relationship("UserModel", back_populates="tables")
  
  entries: Mapped[List["EntryModel"]] = relationship(back_populates="table")
  categories = relationship(
      "CategoryModel",
      secondary=table_category,
      back_populates="tables"
  )

  users: Mapped[List['UserModel']] = relationship(
      "UserModel",
      secondary=user_table,
      back_populates="tables"
  )
