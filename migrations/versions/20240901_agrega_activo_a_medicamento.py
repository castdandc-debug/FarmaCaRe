"""Agrega campo activo a Medicamento

Revision ID: agrega_activo_a_medicamento
Revises: 
Create Date: 2025-09-01 19:10:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'agrega_activo_a_medicamento'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('medicamentos',
        sa.Column('activo', sa.Boolean(), nullable=True)
    )
    # Opcional: poner todos los medicamentos existentes como activos por defecto
    op.execute('UPDATE medicamentos SET activo = TRUE WHERE activo IS NULL;')

def downgrade():
    op.drop_column('medicamentos', 'activo')
