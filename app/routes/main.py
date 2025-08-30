# app/routes/main.py
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Redirige siempre al dashboard. Flask-Login manejará la redirección al login
    # si el usuario no está autenticado.
    return redirect(url_for('main.dashboard'))

@main.route('/dashboard')
@login_required
def dashboard():
    # Verifica el rol del usuario y renderiza la plantilla correcta
    if current_user.rol == 'Administrador':
        return render_template('dashboard_admin.html')
    elif current_user.rol == 'Caja':
        return render_template('dashboard_caja.html')
    else:
        # Si el rol es desconocido, puedes mostrar un error o simplemente redirigir a un lugar seguro.
        # Por ejemplo, una página de error o nuevamente el login con un mensaje.
        return redirect(url_for('auth.login'))

@main.route('/profile')
@login_required
def profile():
    return render_template('perfil.html', name=current_user.nombre)
