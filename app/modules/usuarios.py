# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash
from app.models import db, Usuario

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios')
def lista():
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

@usuarios_bp.route('/usuarios/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        username = request.form['username']
        rol = request.form['rol']
        if Usuario.query.filter_by(username=username).first():
            flash('Error: El usuario ya existe.')
            return redirect(url_for('usuarios.crear'))
        hashed_password = generate_password_hash('123456')
        nuevo = Usuario(username=username, rol=rol)
        nuevo.set_password('123456')
        db.session.add(nuevo)
        db.session.commit()
        flash(f'Usuario "{username}" creado. Contraseña: 123456')
        return redirect(url_for('usuarios.lista'))
    return render_template('crear_usuario.html')

@usuarios_bp.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    u = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        u.username = request.form['username']
        u.rol = request.form['rol']
        db.session.commit()
        flash('Usuario actualizado.')
        return redirect(url_for('usuarios.lista'))
    return render_template('editar_usuario.html', usuario=u)

@usuarios_bp.route('/usuarios/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    u = Usuario.query.get_or_404(id)
    if u.username != 'admin':
        db.session.delete(u)
        db.session.commit()
        flash('Usuario eliminado.')
    else:
        flash('No se puede eliminar el admin.')
    return redirect(url_for('usuarios.lista'))
