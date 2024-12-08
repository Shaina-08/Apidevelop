"""create posts table

Revision ID: a5c64328d13b
Revises: be81360c40f2
Create Date: 2024-12-05 12:35:25.801449

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5c64328d13b'
down_revision: Union[str, None] = 'be81360c40f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
