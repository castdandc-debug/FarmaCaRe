from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, Medicamento, Salida, Cliente, NoHay

ventas_bp = Blueprint('ventas', __name__, template_folder='../templates')

@ventas_bp.route('/lista')
@login_required
def lista():
    ventas = Salida.query.all()
    return render_template('ventas.html', ventas=ventas)

@ventas_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    if request.method == 'POST':
        producto_id = request.form.get('producto_id')
        cantidad = int(request.form.get('cantidad'))
        cliente_id = request.form.get('cliente_id')

        producto = Medicamento.query.get(producto_id)
        if not producto or producto.stock < cantidad:
            flash('Stock insuficiente o producto no encontrado.', 'error')
            return redirect(url_for('ventas.crear'))

        salida = Salida(
            producto_id=producto_id,
            producto_tipo='Medicamento',
            cantidad=cantidad,
            importe_unitario=producto.precio_venta,
            importe_antes_iva=producto.precio_venta * cantidad,
            iva_porcentaje=producto.iva,
            valor_iva=(producto.precio_venta * cantidad * producto.iva / 100),
            importe_total=(producto.precio_venta * cantidad * (1 + producto.iva / 100)),
            cliente_id=cliente_id if cliente_id else None  # Corrección aquí
        )
        db.session.add(salida)
        producto.stock -= cantidad
        db.session.commit()
        flash('Venta registrada exitosamente.', 'success')
        return redirect(url_for('ventas.lista'))

    medicamentos = Medicamento.query.all()
    clientes = Cliente.query.all()
    return render_template('crear_venta.html', medicamentos=medicamentos, clientes=clientes)
