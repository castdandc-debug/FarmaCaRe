# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models import db, Cliente

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/clientes')
def lista():
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

@clientes_bp.route('/clientes/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        
        # Usar .get() para campos opcionales. Si no se proveen, el valor será 'Sin dato'
        rfc = request.form.get('rfc', 'Sin dato')
        contacto = request.form.get('contacto', 'Sin dato')
        telefono = request.form.get('telefono', 'Sin dato')
        direccion = request.form.get('direccion', 'Sin dato')
        
        # La validación para RFC se debe basar en el RFC proporcionado si no es "Sin dato"
        if rfc != 'Sin dato' and Cliente.query.filter_by(rfc=rfc).first():
            flash('Error: RFC ya registrado.')
            return redirect(url_for('clientes.crear'))
        
        cli = Cliente(
            nombre=nombre,
            rfc=rfc,
            contacto=contacto,
            telefono=telefono,
            direccion=direccion
        )
        db.session.add(cli)
        db.session.commit()
        flash('Cliente creado.')
        return redirect(url_for('clientes.lista'))
    return render_template('crear_cliente.html')

@clientes_bp.route('/clientes/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    c = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        c.nombre = request.form['nombre']
        c.rfc = request.form.get('rfc', 'Sin dato')
        c.contacto = request.form.get('contacto', 'Sin dato')
        c.telefono = request.form.get('telefono', 'Sin dato')
        c.direccion = request.form.get('direccion', 'Sin dato')
        db.session.commit()
        flash('Cliente actualizado.')
        return redirect(url_for('clientes.lista'))
    return render_template('editar_cliente.html', cliente=c)

@clientes_bp.route('/clientes/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    c = Cliente.query.get_or_404(id)
    db.session.delete(c)
    db.session.commit()
    flash('Cliente eliminado.')
    return redirect(url_for('clientes.lista'))
