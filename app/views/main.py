from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
import io
import base64
import matplotlib.pyplot as plt
from app.models import Salida

main_bp = Blueprint('main', __name__, template_folder='../templates')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.rol == 'Admin':
        return render_template('dashboard_admin.html')
    return render_template('dashboard_caja.html')

@main_bp.route('/contabilidad')
@login_required
def contabilidad():
    if current_user.rol != 'Admin':
        return redirect(url_for('main.dashboard'))
    ventas = Salida.query.all()
    fig, ax = plt.subplots()
    ax.plot([v.fecha for v in ventas], [v.importe_total for v in ventas])
    ax.set_title('Ventas por Fecha')
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return render_template('contabilidad.html', graph=img_base64)
