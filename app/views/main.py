# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models import db, Usuario

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@main_bp.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html', user=current_user)

@main_bp.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    if request.method == 'POST':
        current_user.username = request.form['username']
        if request.form['password']:
            current_user.set_password(request.form['password'])
        db.session.commit()
        flash('Perfil actualizado correctamente.')
        return redirect(url_for('main.perfil'))
    return render_template('editar_perfil.html', user=current_user)
