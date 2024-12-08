"""add user table

Revision ID: c73aeb7e5633
Revises: 5626be183cc4
Create Date: 2024-12-05 12:48:37.703000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c73aeb7e5633'
down_revision: Union[str, None] = '5626be183cc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users', 
    sa.Column('id', sa.Integer(), nullable=False ),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
              server_default=sa.text('now()'),nullable=False),
    sa.UniqueConstraint('email'),        
    sa.PrimaryKeyConstraint('id')
     
                                        )
    pass


def downgrade():
    op.drop_table('users')
    pass
