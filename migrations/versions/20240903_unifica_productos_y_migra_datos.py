"""Unifica productos, migra datos y elimina tablas viejas

Revision ID: unifica_productos_y_migra_datos
Revises: f3dc6dff893d
Create Date: 2025-09-03 19:56:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column, select

revision = 'unifica_productos_y_migra_datos'
down_revision = 'f3dc6dff893d'
branch_labels = None
depends_on = None

def upgrade():
    connection = op.get_bind()

    # 1. Agregar solo columnas faltantes a productos
    with op.batch_alter_table('productos') as batch_op:
        batch_op.add_column(sa.Column('tipo', sa.String(20), nullable=True))
        batch_op.add_column(sa.Column('codigo_barras', sa.String(50), nullable=True))
        batch_op.add_column(sa.Column('nombre_comercial', sa.String(150), nullable=True))
        batch_op.add_column(sa.Column('nombre_generico', sa.String(150), nullable=True))
        batch_op.add_column(sa.Column('nombre_comun', sa.String(150), nullable=True))
        batch_op.add_column(sa.Column('laboratorio', sa.String(100), nullable=True))
        batch_op.add_column(sa.Column('presentacion', sa.String(100), nullable=True))
        batch_op.add_column(sa.Column('grupo', sa.String(50), nullable=True))
        batch_op.add_column(sa.Column('iva', sa.Float, nullable=True))
        batch_op.add_column(sa.Column('descuento', sa.Float, nullable=True))
        batch_op.add_column(sa.Column('precio_venta', sa.Float, nullable=True))
        batch_op.add_column(sa.Column('punto_reorden', sa.Integer, nullable=True))
        batch_op.add_column(sa.Column('activo', sa.Boolean, nullable=True))
        batch_op.add_column(sa.Column('fecha_modificacion', sa.DateTime, nullable=True))

    # 2. Migrar datos de medicamentos (modelo completo)
    medicamentos = table('medicamentos',
        column('id', sa.Integer),
        column('codigo_barras', sa.String),
        column('nombre_comercial', sa.String),
        column('nombre_generico', sa.String),
        column('laboratorio', sa.String),
        column('presentacion', sa.String),
        column('grupo', sa.String),
        column('iva', sa.Float),
        column('descuento', sa.Float),
        column('precio_venta', sa.Float),
        column('stock', sa.Integer),
        column('punto_reorden', sa.Integer),
        column('activo', sa.Boolean),
        column('fecha_creacion', sa.DateTime),
        column('fecha_modificacion', sa.DateTime),
    )

    productos = table('productos',
        column('id', sa.Integer),
        column('tipo', sa.String),
        column('codigo_barras', sa.String),
        column('nombre_comercial', sa.String),
        column('nombre_generico', sa.String),
        column('nombre_comun', sa.String),
        column('laboratorio', sa.String),
        column('presentacion', sa.String),
        column('grupo', sa.String),
        column('iva', sa.Float),
        column('descuento', sa.Float),
        column('precio_venta', sa.Float),
        column('stock', sa.Integer),
        column('punto_reorden', sa.Integer),
        column('activo', sa.Boolean),
        column('fecha_creacion', sa.DateTime),
        column('fecha_modificacion', sa.DateTime),
        column('proveedor_id', sa.Integer),
        column('nombre', sa.String),
        column('precio', sa.Float),
    )

    med_rows = connection.execute(select(medicamentos)).fetchall()
    for row in med_rows:
        connection.execute(
            productos.insert().values(
                tipo='medicamento',
                codigo_barras=row.codigo_barras,
                nombre_comercial=row.nombre_comercial,
                nombre_generico=row.nombre_generico,
                nombre_comun=None,
                laboratorio=row.laboratorio,
                presentacion=row.presentacion,
                grupo=row.grupo,
                iva=row.iva,
                descuento=row.descuento,
                precio_venta=row.precio_venta,
                stock=row.stock,
                punto_reorden=row.punto_reorden,
                activo=row.activo,
                fecha_creacion=row.fecha_creacion,
                fecha_modificacion=row.fecha_modificacion,
                proveedor_id=None,
                nombre=row.nombre_comercial or row.nombre_generico or "SIN NOMBRE",
                precio=row.precio_venta
            )
        )

    # 3. Migrar datos de dispositivos_medicos (solo columnas reales)
    dispositivos = table('dispositivos_medicos',
        column('id', sa.Integer),
        column('codigo_barras', sa.String),
        column('nombre_comun', sa.String),
        column('nombre_comercial', sa.String),
        column('laboratorio', sa.String),
        column('presentacion', sa.String),
        column('iva', sa.Float),
        column('descuento', sa.Float),
        column('precio_venta', sa.Float),
        column('stock', sa.Integer),
        column('activo', sa.Boolean),
        column('fecha_modificacion', sa.DateTime),  # solo si existe
        # proveedor_id NO EXISTE
    )

    disp_rows = connection.execute(select(dispositivos)).fetchall()
    for row in disp_rows:
        connection.execute(
            productos.insert().values(
                tipo='dispositivo',
                codigo_barras=row.codigo_barras,
                nombre_comercial=row.nombre_comercial,
                nombre_generico=None,
                nombre_comun=row.nombre_comun,
                laboratorio=row.laboratorio,
                presentacion=row.presentacion,
                grupo=None,
                iva=row.iva,
                descuento=row.descuento,
                precio_venta=row.precio_venta,
                stock=row.stock,
                punto_reorden=None,  # no existe en dispositivos_medicos
                activo=row.activo,
                fecha_creacion=None,  # no existe en dispositivos_medicos
                fecha_modificacion=getattr(row, 'fecha_modificacion', None),  # solo si existe
                proveedor_id=None,  # no existe en dispositivos_medicos
                nombre=row.nombre_comun or row.nombre_comercial or "SIN NOMBRE",
                precio=row.precio_venta
            )
        )

    # 4. Eliminar tablas viejas SOLO CUANDO VERIFIQUES LOS DATOS
    # op.drop_table('medicamentos')
    # op.drop_table('dispositivos_medicos')

def downgrade():
    raise Exception("Esta migración no puede ser revertida automáticamente.")
