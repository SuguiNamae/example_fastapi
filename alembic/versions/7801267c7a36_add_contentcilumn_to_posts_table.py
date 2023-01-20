"""add contentcilumn to posts table

Revision ID: 7801267c7a36
Revises: d017c2e10c03
Create Date: 2023-01-20 01:15:26.456751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7801267c7a36'
down_revision = 'd017c2e10c03'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
