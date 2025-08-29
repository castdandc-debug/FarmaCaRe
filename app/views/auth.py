# app/views/auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from app.models import Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.rol == 'admin':
            return redirect(url_for('main.dashboard')) # <--- CAMBIO AQUÍ
        else:
            return redirect(url_for('main.dashboard')) # <--- Y AQUÍ

    if request.method == 'POST':
        nombre_usuario = request.form['username']
        contraseña = request.form['password']
        usuario = Usuario.query.filter_by(nombre=nombre_usuario).first()

        if usuario and check_password_hash(usuario.contraseña, contraseña):
            login_user(usuario)
            if usuario.rol == 'admin':
                return redirect(url_for('main.dashboard')) # <--- CAMBIO AQUÍ
            else:
                return redirect(url_for('main.dashboard')) # <--- Y AQUÍ
        else:
            flash('Nombre de usuario o contraseña incorrectos.')
            return render_template('auth/login.html')

    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
