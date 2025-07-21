from __future__ import annotations

from sqlalchemy import TIMESTAMP, Column, ForeignKey, Table, func
from app.infrastructure.database.connection import Base

user_table = Table(
    "user_table",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("table_id", ForeignKey("table.id"), primary_key=True),
    Column("created_at", TIMESTAMP(timezone=True), server_default=func.now()),
    Column("updated_at", TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
)
