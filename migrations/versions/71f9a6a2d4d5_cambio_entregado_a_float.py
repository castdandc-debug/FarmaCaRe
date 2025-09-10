"""Cambio entregado a Float

Revision ID: 71f9a6a2d4d5
Revises: 117c38e2ded8
Create Date: 2025-09-08 14:24:06.738457

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '71f9a6a2d4d5'
down_revision = '117c38e2ded8'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('cierres_caja', schema=None) as batch_op:
        batch_op.alter_column(
            'entregado',
            existing_type=sa.BOOLEAN(),
            type_=sa.Float(),
            nullable=False,
            postgresql_using="CASE WHEN entregado THEN 1.0 ELSE 0.0 END"
        )

def downgrade():
    with op.batch_alter_table('cierres_caja', schema=None) as batch_op:
        batch_op.alter_column(
            'entregado',
            existing_type=sa.Float(),
            type_=sa.BOOLEAN(),
            nullable=True,
            postgresql_using="CASE WHEN entregado <> 0 THEN true ELSE false END"
        )
