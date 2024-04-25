"""user - add memo

Revision ID: 669f9f2964f8
Revises: eaf13f38b8ea
Create Date: 2024-04-24 17:29:10.871653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '669f9f2964f8'
down_revision: Union[str, None] = 'eaf13f38b8ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('memo', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('User', 'memo')
    # ### end Alembic commands ###