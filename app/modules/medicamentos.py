# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, Medicamento

medicamentos_bp = Blueprint('medicamentos', __name__, url_prefix='/medicamentos')

@medicamentos_bp.route('/')
@login_required
def lista():
    if current_user.rol != 'administrador':
        flash('Acceso denegado.')
        return redirect(url_for('main.dashboard'))

    query = request.args.get('q', '').strip()
    if query:
        meds = Medicamento.query.filter(
            (Medicamento.nombre_comercial.ilike(f'%{query}%')) |
            (Medicamento.nombre_generico.ilike(f'%{query}%')) |
            (Medicamento.codigo_barras.ilike(f'%{query}%')) |
            (Medicamento.laboratorio.ilike(f'%{query}%'))
        ).all()
    else:
        meds = Medicamento.query.all()

    return render_template('medicamentos.html', medicamentos=meds, user=current_user, query=query)

@medicamentos_bp.route('/agregar', methods=['GET', 'POST'])
@login_required
def agregar():
    if current_user.rol != 'administrador':
        flash('Acceso denegado.')
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        med = Medicamento(
            codigo_barras=request.form['codigo_barras'],
            nombre_comercial=request.form['nombre_comercial'],
            nombre_generico=request.form['nombre_generico'] or None,
            laboratorio=request.form['laboratorio'],
            presentacion=request.form['presentacion'] or None,
            grupo=request.form['grupo'],
            iva=float(request.form['iva']),
            precio_venta=float(request.form['precio_venta'])
        )
        db.session.add(med)
        db.session.commit()
        flash('Medicamento agregado exitosamente.')
        return redirect(url_for('medicamentos.lista'))

    return render_template('agregar_medicamento.html', user=current_user)

@medicamentos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    if current_user.rol != 'administrador':
        flash('Acceso denegado.')
        return redirect(url_for('main.dashboard'))

    med = Medicamento.query.get_or_404(id)
    if request.method == 'POST':
        med.codigo_barras = request.form['codigo_barras']
        med.nombre_comercial = request.form['nombre_comercial']
        med.nombre_generico = request.form['nombre_generico'] or None
        med.laboratorio = request.form['laboratorio']
        med.presentacion = request.form['presentacion'] or None
        med.grupo = request.form['grupo']
        med.iva = float(request.form['iva'])
        med.precio_venta = float(request.form['precio_venta'])
        db.session.commit()
        flash('Medicamento actualizado exitosamente.')
        return redirect(url_for('medicamentos.lista'))

    return render_template('editar_medicamento.html', med=med, user=current_user)

@medicamentos_bp.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    if current_user.rol != 'administrador':
        flash('Acceso denegado.')
        return redirect(url_for('main.dashboard'))

    med = Medicamento.query.get_or_404(id)
    db.session.delete(med)
    db.session.commit()
    flash('Medicamento eliminado exitosamente.')
    return redirect(url_for('medicamentos.lista'))
