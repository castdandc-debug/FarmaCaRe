from flask import Blueprint, send_file, render_template
from flask_login import login_required
import pandas as pd
import io
from datetime import datetime

from app.models import Inventario  # Importa tu modelo correctamente

bp = Blueprint('inventario', __name__, url_prefix='/inventario')

@bp.route('/lista')
@login_required
def lista():
    inventarios = Inventario.query.all()
    return render_template('inventario.html', inventarios=inventarios)

@bp.route('/exportar_excel')
@login_required
def exportar_excel():
    inventarios = Inventario.query.all()
    data = []
    for inv in inventarios:
        if hasattr(inv, 'producto') and inv.producto and inv.cantidad > 0:
            data.append({
                "Código": inv.producto.codigo_barras,
                "Nombre": inv.producto.nombre_comercial,
                "Presentación": inv.producto.presentacion,
                "Tipo": inv.producto.tipo,
                "Stock": inv.cantidad,
            })
    df = pd.DataFrame(data) if data else pd.DataFrame(columns=["Código", "Nombre", "Presentación", "Tipo", "Stock"])
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Inventario')
    output.seek(0)
    return send_file(output, download_name="inventario.xlsx", as_attachment=True)

@bp.route('/exportar_pdf')
@login_required
def exportar_pdf():
    inventarios = Inventario.query.all()
    from weasyprint import HTML
    rendered = render_template("inventario_pdf.html", inventarios=inventarios, now=datetime.now)
    pdf = HTML(string=rendered).write_pdf()
    return send_file(io.BytesIO(pdf), download_name="inventario.pdf", as_attachment=True)
