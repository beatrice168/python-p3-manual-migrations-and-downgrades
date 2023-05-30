"""Renaming students to scholars

Revision ID: 53288308b0f4
Revises: 791279dd0760
Create Date: 2023-05-31 00:39:53.932228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53288308b0f4'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')



def downgrade() -> None:
    op.rename_table('scholars', 'students')

