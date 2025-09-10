# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.extensions import db
from app.models import DispositivoMedico, Inventario

dispositivos_bp = Blueprint('dispositivos', __name__)

@dispositivos_bp.route('/dispositivos')
def lista():
    dispositivos = DispositivoMedico.query.all()
    return render_template('dispositivos.html', dispositivos=dispositivos)

@dispositivos_bp.route('/dispositivos/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        codigo_barras = request.form['codigo_barras']
        if DispositivoMedico.query.filter_by(codigo_barras=codigo_barras).first():
            flash('Error: Ese código de barras ya existe.', 'danger')
            return redirect(url_for('dispositivos.agregar'))

        disp = DispositivoMedico(
            codigo_barras=codigo_barras,
            nombre_comercial=request.form['nombre_comercial'],
            nombre_comun=request.form.get('nombre_comun', ''),
            laboratorio=request.form.get('laboratorio', ''),
            presentacion=request.form['presentacion'],
            iva=float(request.form['iva']),
            precio_venta=float(request.form['precio_venta'])
        )
        db.session.add(disp)
        db.session.commit()
        # Crear inventario si se requiere
        inventario = Inventario.query.filter_by(producto_id=disp.id, producto_tipo='dispositivo').first()
        if not inventario:
            inventario = Inventario(producto_id=disp.id, producto_tipo='dispositivo', cantidad=0, punto_reorden=3)
            db.session.add(inventario)
            db.session.commit()
        flash('Dispositivo médico agregado correctamente', 'success')
        return redirect(url_for('dispositivos.lista'))
    return render_template('agregar_dispositivo.html')

@dispositivos_bp.route('/dispositivos/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    disp = DispositivoMedico.query.get_or_404(id)
    if request.method == 'POST':
        # No permitimos editar el inventario aquí
        disp.codigo_barras = request.form['codigo_barras']
        disp.nombre_comercial = request.form['nombre_comercial']
        disp.nombre_comun = request.form.get('nombre_comun', '')
        disp.laboratorio = request.form.get('laboratorio', '')
        disp.presentacion = request.form['presentacion']
        disp.iva = float(request.form['iva'])
        disp.precio_venta = float(request.form['precio_venta'])
        db.session.commit()
        flash('Dispositivo médico actualizado correctamente', 'success')
        return redirect(url_for('dispositivos.lista'))
    return render_template('editar_dispositivo.html', disp=disp)

@dispositivos_bp.route('/dispositivos/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    disp = DispositivoMedico.query.get_or_404(id)
    inventario = Inventario.query.filter_by(producto_id=disp.id, producto_tipo='dispositivo').first()
    if inventario and inventario.cantidad > 0:
        flash('No se puede eliminar el dispositivo, tiene inventario vigente mayor a 0. Puede editarlo pero no eliminarlo.', 'danger')
        return redirect(url_for('dispositivos.lista'))
    db.session.delete(disp)
    db.session.commit()
    flash('Dispositivo médico eliminado correctamente', 'success')
    return redirect(url_for('dispositivos.lista'))
