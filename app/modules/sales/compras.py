from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, send_file
from app.extensions import db
from app.models import Compra, Proveedor, DetalleCompra, Producto, Inventario
from flask_login import current_user, login_required
import json
import io
import pandas as pd

bp = Blueprint('compras', __name__, url_prefix='/compras')

@bp.route('/')
@login_required
def lista():
    compras = Compra.query.all()
    return render_template('compras.html', compras=compras)

@bp.route('/nueva', methods=['GET', 'POST'])
@login_required
def nueva():
    proveedores = Proveedor.query.all()

    if request.method == 'POST':
        proveedor_id = request.form.get('proveedor_id')
        folio_factura = request.form.get('folio_factura')
        carrito = request.form.get('carrito')

        if not proveedor_id or not folio_factura:
            flash('Debes seleccionar un proveedor y capturar el folio de factura.')
            return redirect(url_for('compras.nueva'))
        if not carrito:
            flash('El carrito de productos está vacío.')
            return redirect(url_for('compras.nueva'))

        try:
            items = json.loads(carrito)
        except Exception:
            flash('Error en los datos del carrito.')
            return redirect(url_for('compras.nueva'))

        if not items or not isinstance(items, list):
            flash('Debes agregar al menos un producto válido.')
            return redirect(url_for('compras.nueva'))

        total = sum([float(item['importe']) for item in items if 'importe' in item])
        usuario_id = current_user.id if current_user.is_authenticated else 1

        compra = Compra(proveedor_id=proveedor_id, total=total, usuario_id=usuario_id, folio_factura=folio_factura)
        db.session.add(compra)
        db.session.commit()

        for item in items:
            prod_id = int(item['id'])
            cantidad = int(item['cantidad'])
            precio_unitario = float(item['precio'])
            importe = float(item['importe'])
            descuento = float(item.get('descuento', 0))
            iva = float(item.get('iva', 16))
            tipo = item.get('tipo', 'medicamento')

            prod = Producto.query.filter_by(id=prod_id, tipo=tipo).first()
            if not prod:
                continue

            precio_sin_iva = round(precio_unitario / (1 + iva/100), 2)

            detalle = DetalleCompra(
                compra_id=compra.id,
                producto_id=prod.id,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                precio_sin_iva=precio_sin_iva,
                importe=importe,
                descuento=descuento,
                iva=iva
            )
            db.session.add(detalle)

            inventario = Inventario.query.filter_by(producto_id=prod.id).first()
            if inventario:
                inventario.cantidad += cantidad

        db.session.commit()
        flash('Compra registrada con éxito.')
        return redirect(url_for('compras.lista'))

    return render_template('nueva_compra.html', proveedores=proveedores, usuario_actual=current_user)

@bp.route('/buscar_producto')
@login_required
def buscar_producto():
    q = request.args.get('q', '').strip()
    resultados = []
    if q:
        productos = Producto.query.filter(
            (Producto.nombre_comercial.ilike(f'%{q}%')) |
            (Producto.nombre_generico.ilike(f'%{q}%')) |
            (Producto.nombre_comun.ilike(f'%{q}%')) |
            (Producto.codigo_barras == q)
        ).limit(20).all()
        for p in productos:
            resultados.append({
                'id': p.id,
                'nombre': p.nombre_comercial if p.tipo == 'medicamento' else p.nombre_comun or p.nombre_comercial,
                'codigo': p.codigo_barras,
                'precio': float(p.precio_venta),
                'presentacion': p.presentacion,
                'iva': p.iva,
                'descuento': p.descuento,
                'tipo': p.tipo
            })
    return jsonify(resultados)

@bp.route('/<int:compra_id>/editar', methods=['GET', 'POST'])
@login_required
def editar(compra_id):
    if getattr(current_user, 'rol', None) != "Administrador":
        flash("No tienes permisos para editar compras.")
        return redirect(url_for('compras.lista'))
    compra = Compra.query.get_or_404(compra_id)
    proveedores = Proveedor.query.all()

    if request.method == 'POST':
        compra.folio_factura = request.form.get('folio_factura')
        compra.proveedor_id = request.form.get('proveedor_id')
        carrito = request.form.get('carrito')

        if not carrito:
            flash('El carrito de productos está vacío.')
            return redirect(url_for('compras.editar', compra_id=compra.id))

        try:
            items = json.loads(carrito)
        except Exception:
            flash('Error en los datos del carrito.')
            return redirect(url_for('compras.editar', compra_id=compra.id))

        if not items or not isinstance(items, list):
            flash('Debes agregar al menos un producto válido.')
            return redirect(url_for('compras.editar', compra_id=compra.id))

        # RESTA el inventario de los productos que están en los detalles antiguos
        for detalle in compra.detalles:
            inventario = Inventario.query.filter_by(producto_id=detalle.producto_id).first()
            if inventario:
                if inventario.cantidad < detalle.cantidad:
                    flash(f"No se puede editar la compra porque el inventario de {detalle.producto_id} es insuficiente para revertir la cantidad anterior.", "danger")
                    return redirect(url_for('compras.editar', compra_id=compra.id))
                inventario.cantidad -= detalle.cantidad
            db.session.delete(detalle)
        db.session.commit()

        total = 0
        for item in items:
            prod_id = int(item['id'])
            cantidad = int(item['cantidad'])
            precio_unitario = float(item['precio'])
            importe = float(item['importe'])
            descuento = float(item.get('descuento', 0))
            iva = float(item.get('iva', 16))
            tipo = item.get('tipo', 'medicamento')

            prod = Producto.query.filter_by(id=prod_id, tipo=tipo).first()
            if not prod:
                continue

            precio_sin_iva = round(precio_unitario / (1 + iva/100), 2)

            detalle = DetalleCompra(
                compra_id=compra.id,
                producto_id=prod.id,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                precio_sin_iva=precio_sin_iva,
                importe=importe,
                descuento=descuento,
                iva=iva
            )
            db.session.add(detalle)

            inventario = Inventario.query.filter_by(producto_id=prod.id).first()
            if inventario:
                inventario.cantidad += cantidad

            total += importe

        compra.total = total
        db.session.commit()
        flash("Compra actualizada correctamente.")
        return redirect(url_for('compras.lista'))

    return render_template('editar_compra.html', compra=compra, detalles=compra.detalles, proveedores=proveedores)

@bp.route('/<int:compra_id>/eliminar', methods=['POST'])
@login_required
def eliminar(compra_id):
    if getattr(current_user, 'rol', None) != "Administrador":
        flash("No tienes permisos para eliminar compras.")
        return redirect(url_for('compras.lista'))
    compra = Compra.query.get_or_404(compra_id)
    for detalle in compra.detalles:
        inventario = Inventario.query.filter_by(producto_id=detalle.producto_id).first()
        if inventario:
            if inventario.cantidad < detalle.cantidad:
                flash(f"No se puede eliminar la compra porque el inventario de {detalle.producto_id} es insuficiente para revertir la cantidad.", "danger")
                return redirect(url_for('compras.lista'))
            inventario.cantidad -= detalle.cantidad
        db.session.delete(detalle)
    db.session.delete(compra)
    db.session.commit()
    flash("Compra eliminada correctamente.")
    return redirect(url_for('compras.lista'))

@bp.route('/<int:compra_id>/detalle')
@login_required
def detalle(compra_id):
    compra = Compra.query.get_or_404(compra_id)
    return render_template('detalle_compra.html', compra=compra)

@bp.route('/generar_pedido_excel')
@login_required
def generar_pedido_excel():
    # Consulta todos los inventarios y productos
    productos_faltantes = (
        db.session.query(Inventario, Producto)
        .join(Producto, Inventario.producto_id == Producto.id)
        .filter(Inventario.cantidad < Inventario.punto_reorden)
        .all()
    )

    data = []
    for inv, prod in productos_faltantes:
        punto_reorden = inv.punto_reorden if inv.punto_reorden is not None else prod.punto_reorden or 0
        cantidad_actual = inv.cantidad if inv.cantidad is not None else 0
        cantidad_faltante = max(punto_reorden - cantidad_actual, 0)
        data.append({
            "Código de barras": prod.codigo_barras,
            "Nombre Comercial": prod.nombre_comercial,
            "Nombre Genérico": prod.nombre_generico,
            "Presentación": prod.presentacion,
            "Cantidad en Inventario": cantidad_actual,
            "Punto de Reorden": punto_reorden,
            "Cantidad Faltante": cantidad_faltante
        })

    # Si no hay productos faltantes, regresa un Excel vacío con encabezados
    df = pd.DataFrame(data)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Pedido")
    output.seek(0)
    return send_file(
        output,
        download_name="pedido_productos_faltantes.xlsx",
        as_attachment=True,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
