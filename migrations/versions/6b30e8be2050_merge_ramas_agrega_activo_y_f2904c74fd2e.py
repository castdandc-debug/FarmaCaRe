"""Merge ramas agrega_activo y f2904c74fd2e

Revision ID: 6b30e8be2050
Revises: agrega_activo_a_medicamento, f2904c74fd2e
Create Date: 2025-09-01 13:10:49.476481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b30e8be2050'
down_revision = ('agrega_activo_a_medicamento', 'f2904c74fd2e')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
