"""testing

Revision ID: bdda07b24b3a
Revises: 499ff08333ee
Create Date: 2024-12-08 12:36:47.260238

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bdda07b24b3a'
down_revision: Union[str, None] = '499ff08333ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('Posts', sa.Column('Shaina', sa.String(), nullable=False))
    op.create_foreign_key('fk_posts_Shaina',source_table='Posts',referent_table='users',local_cols=['Shaina'],remote_cols=['email'])

    pass


def downgrade() -> None:
    op.drop_constraint('fk_posts_Shaina', 'Posts', type_='foreignkey')
    op.drop_column('Posts', 'Shaina')
    pass
