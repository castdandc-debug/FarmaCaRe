from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return redirect(url_for('auth.login'))

@main_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.rol == 'Administrador':
        return render_template('dashboard_admin.html')
    elif current_user.rol == 'Caja':
        return render_template('dashboard_caja.html')
    else:
        return render_template('dashboard.html')
