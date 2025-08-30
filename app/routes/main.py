# app/routes/main.py

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Si el usuario ya está autenticado, redirigir al dashboard
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    # Si no lo está, redirigir a la página de login
    return redirect(url_for('auth.login'))

@main.route('/dashboard')
@login_required
def dashboard():
    # Verifica el rol del usuario y renderiza la plantilla correcta
    if current_user.rol == 'Administrador':
        return render_template('dashboard_admin.html')
    elif current_user.rol == 'Caja':
        return render_template('dashboard_caja.html')
    else:
        # Si el rol es desconocido, redirige al login con un mensaje de error.
        return redirect(url_for('auth.login'))

@main.route('/profile')
@login_required
def profile():
    return render_template('perfil.html', name=current_user.nombre)
