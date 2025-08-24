# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models import db, Venta, Cliente, Usuario, Medicamento

ventas_bp = Blueprint('ventas', __name__)

@ventas_bp.route('/ventas')
def lista():
    ventas = Venta.query.all()
    return render_template('ventas.html', ventas=ventas)

@ventas_bp.route('/ventas/nueva', methods=['GET', 'POST'])
def nueva():
    clientes = Cliente.query.all()
    medicamentos = Medicamento.query.all()
    if request.method == 'POST':
        cliente_id = int(request.form['cliente_id'])
        items = []
        total = 0
        for key, value in request.form.items():
            if key.startswith('med_') and value:
                med_id = int(key.replace('med_', ''))
                cantidad = int(value)
                med = Medicamento.query.get(med_id)
                if med and med.stock >= cantidad:
                    items.append((med, cantidad))
                    total += med.precio_venta * cantidad
                else:
                    flash(f'Stock insuficiente para {med.nombre_comercial}')
                    return redirect(url_for('ventas.nueva'))

        # Crear venta
        venta = Venta(cliente_id=cliente_id, total=total, usuario_id=1)
        db.session.add(venta)
        db.session.commit()

        # Actualizar stock
        for med, cantidad in items:
            med.stock -= cantidad
        db.session.commit()

        flash('Venta realizada con éxito.')
        return redirect(url_for('ventas.lista'))

    return render_template('nueva_venta.html', clientes=clientes, medicamentos=medicamentos)
