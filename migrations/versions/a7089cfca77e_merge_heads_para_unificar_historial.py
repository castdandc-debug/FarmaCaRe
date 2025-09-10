"""Merge heads para unificar historial

Revision ID: a7089cfca77e
Revises: unifica_productos_y_migra_datos, e22adf2dd6da
Create Date: 2025-09-03 14:43:23.300333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7089cfca77e'
down_revision = ('unifica_productos_y_migra_datos', 'e22adf2dd6da')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
