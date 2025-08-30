# app/routes/main.py
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Si el usuario ya está autenticado, lo enviamos directamente al dashboard.
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    # Si no lo está, lo redirigimos al login
    return redirect(url_for('auth.login'))

@main.route('/dashboard')
@login_required
def dashboard():
    # Lógica para renderizar el dashboard según el rol del usuario.
    if current_user.rol == 'Administrador':
        return render_template('dashboard_admin.html')
    elif current_user.rol == 'Caja':
        return render_template('dashboard_caja.html')
    else:
        # En caso de que el rol no sea reconocido, lo redirigimos al login.
        return redirect(url_for('auth.login'))

@main.route('/profile')
@login_required
def profile():
    return render_template('perfil.html', name=current_user.nombre)
