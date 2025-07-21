from __future__ import annotations

from sqlalchemy import TIMESTAMP, Column, ForeignKey, Table, func
from app.infrastructure.database.connection import Base

table_category = Table(
    "table_category",
    Base.metadata,
    Column("category_id", ForeignKey("category.id"), primary_key=True),
    Column("table_id", ForeignKey("table.id"), primary_key=True),
    Column("created_at", TIMESTAMP(timezone=True), server_default=func.now()),
    Column("updated_at", TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
)