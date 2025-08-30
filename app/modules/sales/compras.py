# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models import db, Compra, Proveedor

compras_bp = Blueprint('compras', __name__)

@compras_bp.route('/compras')
def lista():
    compras = Compra.query.all()
    return render_template('compras.html', compras=compras)

@compras_bp.route('/compras/nueva', methods=['GET', 'POST'])
def nueva():
    proveedores = Proveedor.query.all()
    if request.method == 'POST':
        proveedor_id = int(request.form['proveedor_id'])
        items = []
        total = 0
        for key, value in request.form.items():
            if key.startswith('med_') and value:
                med_id = int(key.replace('med_', ''))
                cantidad = int(value)
                med = Medicamento.query.get(med_id)
                if med:
                    items.append((med, cantidad))
                    total += med.precio_venta * cantidad
                else:
                    flash(f'Medicamento no encontrado.')
                    return redirect(url_for('compras.nueva'))

        # Crear compra
        compra = Compra(proveedor_id=proveedor_id, total=total, usuario_id=1)
        db.session.add(compra)
        db.session.commit()

        # Actualizar stock
        for med, cantidad in items:
            med.stock += cantidad
        db.session.commit()

        flash('Compra registrada con éxito.')
        return redirect(url_for('compras.lista'))

    return render_template('nueva_compra.html', proveedores=proveedores)
