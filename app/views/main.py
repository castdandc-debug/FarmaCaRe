# -*- coding: utf-8 -*-
from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required

main_bp = Blueprint('main', __name__)

# Ruta raíz: redirige al login
@main_bp.route('/')
def index():
    return redirect(url_for('auth.login'))

# Dashboard (requiere login)
@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
