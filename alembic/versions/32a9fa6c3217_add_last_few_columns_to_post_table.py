"""add last few columns to post table

Revision ID: 32a9fa6c3217
Revises: f2582d760679
Create Date: 2024-12-08 12:11:46.764130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32a9fa6c3217'
down_revision: Union[str, None] = 'f2582d760679'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('posts', sa.Column('published', sa.BOOLEAN, server_default='TRUE', nullable=False))

    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
