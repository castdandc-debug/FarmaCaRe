# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models import db, Medicamento

medicamentos_bp = Blueprint('medicamentos', __name__)

@medicamentos_bp.route('/medicamentos')
def lista():
    medicamentos = Medicamento.query.all()
    return render_template('medicamentos.html', medicamentos=medicamentos)

@medicamentos_bp.route('/medicamentos/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        med = Medicamento(
            codigo_barras=request.form['codigo_barras'],
            nombre_comercial=request.form['nombre_comercial'],
            nombre_generico=request.form['nombre_generico'],
            laboratorio=request.form['laboratorio'],
            presentacion=request.form['presentacion'],
            grupo=request.form['grupo'],
            iva=float(request.form['iva']),
            precio_venta=float(request.form['precio_venta']),
            stock=int(request.form['stock'])
        )
        db.session.add(med)
        db.session.commit()
        flash('Medicamento agregado correctamente')
        return redirect(url_for('medicamentos.lista'))
    return render_template('agregar_medicamento.html')

@medicamentos_bp.route('/medicamentos/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    med = Medicamento.query.get_or_404(id)
    if request.method == 'POST':
        med.codigo_barras = request.form['codigo_barras']
        med.nombre_comercial = request.form['nombre_comercial']
        med.nombre_generico = request.form['nombre_generico']
        med.laboratorio = request.form['laboratorio']
        med.presentacion = request.form['presentacion']
        med.grupo = request.form['grupo']
        med.iva = float(request.form['iva'])
        med.precio_venta = float(request.form['precio_venta'])
        med.stock = int(request.form['stock'])
        db.session.commit()
        flash('Medicamento actualizado correctamente')
        return redirect(url_for('medicamentos.lista'))
    return render_template('editar_medicamento.html', med=med)
