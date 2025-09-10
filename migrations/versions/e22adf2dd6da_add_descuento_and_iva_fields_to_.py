"""Add descuento and iva fields to DetalleCompra

Revision ID: e22adf2dd6da
Revises: f1bd564d60e3
Create Date: 2025-09-02 19:20:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e22adf2dd6da'
down_revision = 'f1bd564d60e3'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('detalle_compra', schema=None) as batch_op:
        batch_op.add_column(sa.Column('descuento', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('iva', sa.Float(), nullable=True))

    # Establecer default para registros existentes
    op.execute("UPDATE detalle_compra SET descuento = 0 WHERE descuento IS NULL;")
    op.execute("UPDATE detalle_compra SET iva = 16 WHERE iva IS NULL;")

    # Ahora sí, hacer NOT NULL
    with op.batch_alter_table('detalle_compra', schema=None) as batch_op:
        batch_op.alter_column('descuento', nullable=False, existing_type=sa.Float())
        batch_op.alter_column('iva', nullable=False, existing_type=sa.Float())

def downgrade():
    with op.batch_alter_table('detalle_compra', schema=None) as batch_op:
        batch_op.drop_column('descuento')
        batch_op.drop_column('iva')
