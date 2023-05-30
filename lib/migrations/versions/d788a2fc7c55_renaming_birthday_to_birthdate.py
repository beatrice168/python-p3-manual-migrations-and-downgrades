"""Renaming birthday to birthdate

Revision ID: d788a2fc7c55
Revises: 53288308b0f4
Create Date: 2023-05-31 00:55:38.604207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd788a2fc7c55'
down_revision = '53288308b0f4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
