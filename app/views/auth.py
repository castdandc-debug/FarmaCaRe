# app/views/auth.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from app.models import Usuario
from app.forms import LoginForm

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Si el usuario ya está autenticado, lo enviamos directamente al dashboard.
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(usuario=form.username.data).first()
        if user and check_password_hash(user.clave_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            # Redirige al usuario al dashboard después de un inicio de sesión exitoso.
            return redirect(url_for('main.dashboard'))
        else:
            flash('Usuario o contraseña inválidos.')

    return render_template('login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))
