from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.models.base import BaseModelWithTimestamps

class TableCategoryModel(BaseModelWithTimestamps):
    __tablename__ = "table_category"

    table_id: Mapped[str] = mapped_column(ForeignKey("table.id"), primary_key=True)
    category_id: Mapped[str] = mapped_column(ForeignKey("category.id"), primary_key=True)