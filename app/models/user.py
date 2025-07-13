from typing import List
from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.orm import Mapped, relationship

from app.models.base import BaseModelWithTimestamps
from app.models.category import CategoryModel
from app.models.entry import EntryModel
from app.models.entry_user_percentage import EntryUserPercentageModel
from app.models.table import TableModel
class UserModel(BaseModelWithTimestamps):
    __tablename__ = "user"

    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=True)
    is_active = Column(Boolean, default = False)
    token = Column(String, default = None, nullable=True)
    token_expiration = Column(DateTime, default = None, nullable=True)

    categories: Mapped[List["CategoryModel"]] = relationship(back_populates="user")
    entries: Mapped[List["EntryModel"]] = relationship(back_populates="user")
    tables: Mapped[List["TableModel"]] = relationship(back_populates="user")
    entry_user_percentages: Mapped[List["EntryUserPercentageModel"]] = relationship(back_populates="user")
