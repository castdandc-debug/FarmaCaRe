from flask import Blueprint, render_template, request
from app.extensions import db
from app.models.inventario import Inventario
from app.models import Producto
from flask_login import login_required, current_user

bp = Blueprint('reportes', __name__, url_prefix='/reportes')

# Informe General
@bp.route('/informe')
@login_required
def informe():
    return render_template('reportes/informe.html', usuario_actual=current_user)

# Cortes de Caja
@bp.route('/cortes_caja')
@login_required
def cortes_caja():
    return render_template('reportes/cortes_caja.html', usuario_actual=current_user)

# Kardex
@bp.route('/kardex')
@login_required
def kardex():
    return render_template('reportes/kardex.html', usuario_actual=current_user)

# Inventarios (ya lo tenías)
@bp.route('/inventarios', methods=['GET'])
@login_required
def inventarios():
    filtro_tipo = request.args.get('tipo_producto', '')
    buscar = request.args.get('buscar', '')
    query = Inventario.query.join(Producto).filter(Producto.activo == True)
    if filtro_tipo:
        query = query.filter(Producto.tipo == filtro_tipo)
    if buscar:
        query = query.filter(
            (Producto.nombre_comercial.ilike(f"%{buscar}%")) |
            (Producto.nombre_generico.ilike(f"%{buscar}%")) |
            (Producto.presentacion.ilike(f"%{buscar}%"))
        )
    inventarios = query.all()
    return render_template('inventario.html', inventarios=inventarios, usuario_actual=current_user)

# Ajustes de Inventario
@bp.route('/ajustes_inventario')
@login_required
def ajustes_inventario():
    return render_template('reportes/ajustes_inventario.html', usuario_actual=current_user)

# No Hay
@bp.route('/no_hay')
@login_required
def no_hay():
    return render_template('reportes/nohay.html', usuario_actual=current_user)

# Exportar Excel
@bp.route('/exportar_excel')
@login_required
def exportar_excel():
    # Aquí irá la lógica real de exportación
    return "Funcionalidad de exportar a Excel pendiente"

# Exportar PDF
@bp.route('/exportar_pdf')
@login_required
def exportar_pdf():
    # Aquí irá la lógica real de exportación
    return "Funcionalidad de exportar a PDF pendiente"
