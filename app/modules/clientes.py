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
        cedula = request.form['cedula']
        if Cliente.query.filter_by(cedula=cedula).first():
            flash('Cédula ya registrada.')
            return redirect(url_for('clientes.crear'))
        cli = Cliente(
            cedula=cedula,
            nombre=request.form['nombre'],
            telefono=request.form['telefono'],
            direccion=request.form['direccion']
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
        c.cedula = request.form['cedula']
        c.nombre = request.form['nombre']
        c.telefono = request.form['telefono']
        c.direccion = request.form['direccion']
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
