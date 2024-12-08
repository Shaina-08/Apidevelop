"""add new column

Revision ID: 5626be183cc4
Revises: a5c64328d13b
Create Date: 2024-12-05 12:42:20.269364

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5626be183cc4'
down_revision: Union[str, None] = 'a5c64328d13b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
