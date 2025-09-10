# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.extensions import db
from app.models import Medicamento, Inventario

medicamentos_bp = Blueprint('medicamentos', __name__)

@medicamentos_bp.route('/medicamentos')
def lista():
    medicamentos = Medicamento.query.all()
    return render_template('medicamentos.html', medicamentos=medicamentos)

@medicamentos_bp.route('/medicamentos/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        codigo_barras = request.form['codigo_barras']
        if Medicamento.query.filter_by(codigo_barras=codigo_barras).first():
            flash('Error: Ese código de barras ya existe.', 'danger')
            return redirect(url_for('medicamentos.agregar'))

        med = Medicamento(
            codigo_barras=codigo_barras,
            nombre_comercial=request.form['nombre_comercial'],
            nombre_generico=request.form['nombre_generico'],
            laboratorio=request.form['laboratorio'],
            presentacion=request.form['presentacion'],
            grupo=request.form['grupo'],
            iva=float(request.form['iva']),
            precio_venta=float(request.form['precio_venta'])
        )
        db.session.add(med)
        db.session.commit()
        # Crear inventario si se requiere
        inventario = Inventario.query.filter_by(producto_id=med.id, producto_tipo='medicamento').first()
        if not inventario:
            inventario = Inventario(producto_id=med.id, producto_tipo='medicamento', cantidad=0, punto_reorden=3)
            db.session.add(inventario)
            db.session.commit()
        flash('Medicamento agregado correctamente', 'success')
        return redirect(url_for('medicamentos.lista'))
    return render_template('agregar_medicamento.html')

@medicamentos_bp.route('/medicamentos/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    med = Medicamento.query.get_or_404(id)
    if request.method == 'POST':
        # No permitimos editar el inventario aquí
        med.codigo_barras = request.form['codigo_barras']
        med.nombre_comercial = request.form['nombre_comercial']
        med.nombre_generico = request.form['nombre_generico']
        med.laboratorio = request.form['laboratorio']
        med.presentacion = request.form['presentacion']
        med.grupo = request.form['grupo']
        med.iva = float(request.form['iva'])
        med.precio_venta = float(request.form['precio_venta'])
        db.session.commit()
        flash('Medicamento actualizado correctamente', 'success')
        return redirect(url_for('medicamentos.lista'))
    return render_template('editar_medicamento.html', med=med)

@medicamentos_bp.route('/medicamentos/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    med = Medicamento.query.get_or_404(id)
    inventario = Inventario.query.filter_by(producto_id=med.id, producto_tipo='medicamento').first()
    if inventario and inventario.cantidad > 0:
        flash('No se puede eliminar el medicamento, tiene inventario vigente mayor a 0. Puede editarlo pero no eliminarlo.', 'danger')
        return redirect(url_for('medicamentos.lista'))
    db.session.delete(med)
    db.session.commit()
    flash('Medicamento eliminado correctamente', 'success')
    return redirect(url_for('medicamentos.lista'))
