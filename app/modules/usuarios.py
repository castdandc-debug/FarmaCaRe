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

        # Verificar si ya existe el usuario
        if Usuario.query.filter_by(username=username).first():
            flash('Error: El usuario ya existe.')
            return redirect(url_for('usuarios.crear'))

        # Crear usuario con contraseña por defecto
        password_default = '123456'
        hashed_password = generate_password_hash(password_default)

        nuevo_usuario = Usuario(
            username=username,
            password=hashed_password,
            rol=rol
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash(f'Usuario "{username}" creado con éxito. Contraseña temporal: {password_default}')
        return redirect(url_for('usuarios.lista'))

    return render_template('crear_usuario.html')

@usuarios_bp.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        usuario.username = request.form['username']
        usuario.rol = request.form['rol']
        db.session.commit()
        flash('Usuario actualizado correctamente.')
        return redirect(url_for('usuarios.lista'))
    return render_template('editar_usuario.html', usuario=usuario)

@usuarios_bp.route('/usuarios/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    usuario = Usuario.query.get_or_404(id)
    if usuario.username == 'admin':
        flash('No se puede eliminar el usuario administrador principal.')
    else:
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuario eliminado correctamente.')
    return redirect(url_for('usuarios.lista'))
