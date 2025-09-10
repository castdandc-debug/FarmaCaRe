# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.extensions import db
from app.models import Proveedor

proveedores_bp = Blueprint('proveedores', __name__)

@proveedores_bp.route('/proveedores')
def lista():
    proveedores = Proveedor.query.all()
    return render_template('proveedores.html', proveedores=proveedores)

@proveedores_bp.route('/proveedores/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        rfc = request.form['rfc']
        if Proveedor.query.filter_by(rfc=rfc).first():
            flash('El RFC ya está registrado.', 'danger')
            return redirect(url_for('proveedores.crear'))
        p = Proveedor(
            rfc=rfc,
            nombre=request.form['nombre'],
            telefono=request.form['telefono'],
            direccion=request.form['direccion'],
            email=request.form['email']
        )
        db.session.add(p)
        db.session.commit()
        flash('Proveedor creado correctamente.', 'success')
        return redirect(url_for('proveedores.lista'))
    return render_template('agregar_proveedor.html')

@proveedores_bp.route('/proveedores/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    p = Proveedor.query.get_or_404(id)
    if request.method == 'POST':
        p.rfc = request.form['rfc']
        p.nombre = request.form['nombre']
        p.telefono = request.form['telefono']
        p.direccion = request.form['direccion']
        p.email = request.form['email']
        db.session.commit()
        flash('Proveedor actualizado correctamente.', 'success')
        return redirect(url_for('proveedores.lista'))
    return render_template('editar_proveedor.html', proveedor=p)

@proveedores_bp.route('/proveedores/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    p = Proveedor.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    flash('Proveedor eliminado correctamente.', 'success')
    return redirect(url_for('proveedores.lista'))
