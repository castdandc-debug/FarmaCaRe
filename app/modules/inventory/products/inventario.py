from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, Inventario, Medicamento, DispositivoMedico, AjusteInventario

inventario_bp = Blueprint('inventario', __name__, template_folder='../templates')

@inventario_bp.route('/lista')
@login_required
def lista():
    inventarios = Inventario.query.all()
    return render_template('inventario.html', inventarios=inventarios)

@inventario_bp.route('/ajustar/<string:tipo>/<int:producto_id>', methods=['GET', 'POST'])
@login_required
def ajustar(tipo, producto_id):
    if tipo == 'Medicamento':
        producto = Medicamento.query.get_or_404(producto_id)
    elif tipo == 'Dispositivo':
        producto = DispositivoMedico.query.get_or_404(producto_id)
    else:
        flash('Tipo de producto no válido.', 'error')
        return redirect(url_for('inventario.lista'))

    inventario = Inventario.query.filter_by(producto_id=producto_id, producto_tipo=tipo).first()
    if not inventario:
        inventario = Inventario(producto_id=producto_id, producto_tipo=tipo, cantidad=producto.stock)
        db.session.add(inventario)
        db.session.commit()

    if request.method == 'POST':
        cantidad_ajuste = int(request.form.get('cantidad_ajuste'))
        razon = request.form.get('razon')
        ajuste = AjusteInventario(
            producto_id=producto_id,
            producto_tipo=tipo,
            cantidad_ajuste=cantidad_ajuste,
            razon=razon,
            usuario_id=current_user.id
        )
        db.session.add(ajuste)
        inventario.cantidad += cantidad_ajuste
        db.session.commit()
        flash('Ajuste de inventario registrado exitosamente.', 'success')
        return redirect(url_for('inventario.lista'))

    return render_template('ajuste_inventario.html', producto=producto, inventario=inventario)
