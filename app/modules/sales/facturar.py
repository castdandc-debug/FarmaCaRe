from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models import Salida, Cliente

bp = Blueprint('facturar', __name__, url_prefix='/facturar', template_folder='../templates')

@bp.route('/<int:nota_id>', methods=['GET', 'POST'])
@login_required
def facturar(nota_id):
    nota = Salida.query.get_or_404(nota_id)
    if getattr(nota, 'eliminada', False):
        flash('Nota eliminada o no existe.', 'error')
        return redirect(url_for('ventas.lista'))
    if request.method == 'POST':
        if not nota.cliente_id:
            cliente_nombre = request.form.get('cliente_nombre')
            cliente_rfc = request.form.get('cliente_rfc')
            cliente = Cliente.query.filter_by(rfc=cliente_rfc).first()
            if not cliente:
                cliente = Cliente(nombre=cliente_nombre, rfc=cliente_rfc)
                db.session.add(cliente)
                db.session.commit()
            nota.cliente_id = cliente.id
            db.session.commit()
        flash('Factura generada exitosamente.', 'success')
        return redirect(url_for('ventas.lista'))
    return render_template('factura.html', nota=nota)
