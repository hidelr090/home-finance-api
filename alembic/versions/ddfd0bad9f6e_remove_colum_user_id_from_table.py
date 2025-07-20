"""remove colum user_id from table

Revision ID: ddfd0bad9f6e
Revises: f65e454d61e0
Create Date: 2025-07-20 12:48:39.509341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ddfd0bad9f6e'
down_revision: Union[str, None] = 'f65e454d61e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('table', 'user_id')    
    pass


def downgrade() -> None:
    op.add_column('table', sa.Column('user_id', sa.UUID, nullable=False))
    pass
