"""Automatic migration based on schema update

Revision ID: 348a6767c89c
Revises: 4e0b43a76b8f
Create Date: 2024-09-08 13:16:59.403889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '348a6767c89c'
down_revision: Union[str, None] = '4e0b43a76b8f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###