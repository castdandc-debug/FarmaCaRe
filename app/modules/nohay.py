from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, NoHay

nohay_bp = Blueprint('nohay', __name__, template_folder='../templates')

@nohay_bp.route('/lista')
@login_required
def lista():
    nohays = NoHay.query.all()
    return render_template('nohay.html', nohays=nohays)

@nohay_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        tipo = request.form.get('tipo')
        descripcion = request.form.get('descripcion')

        nohay = NoHay(nombre=nombre, tipo=tipo, descripcion=descripcion)
        db.session.add(nohay)
        db.session.commit()
        flash('Registro "No Hay" creado exitosamente.', 'success')
        return redirect(url_for('nohay.lista'))

    return render_template('nohay.html')
