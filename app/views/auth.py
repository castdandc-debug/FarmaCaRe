# app/views/auth.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Si el usuario ya está autenticado, lo enviamos directamente al dashboard
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        contraseña = request.form.get('contraseña')
        
        # Buscar usuario por nombre (no por username)
        user = Usuario.query.filter_by(nombre=nombre).first()
        
        # Verificar si el usuario existe y la contraseña es correcta
        if user and user.check_password(contraseña):
            login_user(user, remember=False)
            flash(f'Bienvenido {user.nombre}', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión exitosamente', 'info')
    return redirect(url_for('auth.login'))
