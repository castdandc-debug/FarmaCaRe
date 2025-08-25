# app/routes/main.py
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Si el usuario no está autenticado, redirigir a la página de inicio de sesión.
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    
    # Redirigir al dashboard según el rol del usuario
    return redirect(url_for('main.dashboard'))

@main.route('/dashboard')
@login_required
def dashboard():
    if current_user.rol == 'Administrador':
        return render_template('dashboard_admin.html')
    elif current_user.rol == 'Caja':
        return render_template('dashboard_caja.html')
    else:
        # En caso de un rol no reconocido, redirigir al login.
        return redirect(url_for('auth.login'))

@main.route('/profile')
@login_required
def profile():
    return render_template('perfil.html', name=current_user.nombre)
