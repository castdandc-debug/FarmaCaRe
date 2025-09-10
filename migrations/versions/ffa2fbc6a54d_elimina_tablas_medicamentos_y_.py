"""Elimina tablas medicamentos y dispositivos_medicos

Revision ID: ffa2fbc6a54d
Revises: a7089cfca77e
Create Date: 2025-09-03 22:13:46.187398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffa2fbc6a54d'
down_revision = 'a7089cfca77e'
branch_labels = None
depends_on = None


def upgrade():
    # Elimina la restricción que depende de medicamentos
    op.drop_constraint('detalle_compra_producto_id_fkey', 'detalle_compra', type_='foreignkey')
    # Si hay otras restricciones similares, repite con sus nombres

    # Ahora elimina las tablas
    op.drop_table('medicamentos')
    op.drop_table('dispositivos_medicos')

def downgrade():
    raise Exception("Esta migración no puede revertirse automáticamente.")
