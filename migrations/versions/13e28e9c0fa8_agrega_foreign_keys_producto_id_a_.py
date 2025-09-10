"""Agrega foreign keys producto_id a productos

Revision ID: 13e28e9c0fa8
Revises: ffa2fbc6a54d
Create Date: 2025-09-04 06:17:40.257184

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '13e28e9c0fa8'
down_revision = 'ffa2fbc6a54d'
branch_labels = None
depends_on = None

def upgrade():
    # Las tablas medicamentos y dispositivos_medicos ya no existen, por eso no intentamos eliminarlas.

    # Elimina columnas tipo_producto y producto_tipo si existen y agrega las FKs
    with op.batch_alter_table('ajustes_inventario', schema=None) as batch_op:
        try:
            batch_op.drop_column('tipo_producto')
        except Exception:
            pass  # Si ya no existe, continúa
        batch_op.create_foreign_key(
            'ajustes_inventario_producto_id_fkey',
            'productos',
            ['producto_id'], ['id']
        )

    with op.batch_alter_table('inventario', schema=None) as batch_op:
        try:
            batch_op.drop_column('tipo_producto')
        except Exception:
            pass
        batch_op.create_foreign_key(
            'inventario_producto_id_fkey',
            'productos',
            ['producto_id'], ['id']
        )

    with op.batch_alter_table('detalle_compra', schema=None) as batch_op:
        batch_op.create_foreign_key(
            'detalle_compra_producto_id_fkey',
            'productos',
            ['producto_id'], ['id']
        )

    with op.batch_alter_table('entradas', schema=None) as batch_op:
        try:
            batch_op.drop_column('tipo_producto')
        except Exception:
            pass
        batch_op.create_foreign_key(
            'entradas_producto_id_fkey',
            'productos',
            ['producto_id'], ['id']
        )

    with op.batch_alter_table('salidas', schema=None) as batch_op:
        try:
            batch_op.drop_column('producto_tipo')
        except Exception:
            pass
        batch_op.create_foreign_key(
            'salidas_producto_id_fkey',
            'productos',
            ['producto_id'], ['id']
        )

    # NOT NULL y UNIQUE en productos, solo si necesitas y si los datos están correctos
    with op.batch_alter_table('productos', schema=None) as batch_op:
        batch_op.alter_column('tipo', nullable=False)
        batch_op.alter_column('codigo_barras', nullable=False)
        batch_op.alter_column('nombre_comercial', nullable=False)
        batch_op.alter_column('precio_venta', nullable=False)
        batch_op.create_unique_constraint('uq_productos_codigo_barras', ['codigo_barras'])
        try:
            batch_op.drop_column('precio')
        except Exception:
            pass
        try:
            batch_op.drop_column('descripcion')
        except Exception:
            pass
        try:
            batch_op.drop_column('nombre')
        except Exception:
            pass

def downgrade():
    raise Exception("Esta migración no puede revertirse automáticamente.")
