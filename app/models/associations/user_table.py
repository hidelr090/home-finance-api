from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.models.base import BaseModelWithTimestamps

class UserTableModel(BaseModelWithTimestamps):
    __tablename__ = "user_table"

    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"), primary_key=True)
    table_id: Mapped[str] = mapped_column(ForeignKey("table.id"), primary_key=True)
