"""empty message

Revision ID: fb7a9a1a69dd
Revises: c73aeb7e5633
Create Date: 2024-12-08 12:05:12.528090

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb7a9a1a69dd'
down_revision: Union[str, None] = 'c73aeb7e5633'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
