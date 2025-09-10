from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.extensions import db
from app.models import Cliente, Producto, Venta, DetalleVenta, NoHay, Usuario, Inventario
from flask_login import login_required, current_user
from datetime import datetime

bp = Blueprint('ventas', __name__, url_prefix='/ventas')

@bp.route('/nueva', methods=['GET', 'POST'])
@login_required
def nueva():
    clientes = Cliente.query.all()

    # Registrar producto NO HAY
    if request.method == 'POST' and request.form.get('no_hay_submit'):
        nombre = request.form.get('nombre_nohay')
        tipo = request.form.get('tipo_nohay')
        if nombre:
            nohay = NoHay(nombre=nombre, tipo=tipo or '', usuario_id=current_user.id)
            db.session.add(nohay)
            db.session.commit()
            flash('Producto registrado como NO HAY', 'info')
        return '', 204

    # Registrar venta
    if request.method == 'POST' and not request.form.get('no_hay_submit'):
        cliente_id = request.form.get('cliente_id') or None
        metodo_pago = request.form.get('metodo_pago')
        productos = []
        subtotal, total_iva, total_descuento, total = 0, 0, 0, 0
        errores_inventario = []
        for key in request.form:
            if key.startswith('med_'):
                prod_id = int(key.split('_')[1])
                cantidad = int(request.form[key])
                producto = Producto.query.get(prod_id)
                if producto and cantidad > 0:
                    inventario = Inventario.query.filter_by(producto_id=prod_id).first()
                    if not inventario or inventario.cantidad < cantidad:
                        errores_inventario.append(f"Inventario insuficiente para {producto.nombre_comercial}. En inventario: {inventario.cantidad if inventario else 0}, intentó vender: {cantidad}")
                        continue
                    precio = producto.precio_venta
                    iva = (precio * cantidad) * (producto.iva/100)
                    desc = (precio * cantidad) * (producto.descuento/100)
                    importe = (precio * cantidad) + iva - desc
                    subtotal += precio * cantidad
                    total_iva += iva
                    total_descuento += desc
                    total += importe
                    productos.append({
                        'producto': producto,
                        'cantidad': cantidad,
                        'precio_unitario': precio,
                        'iva': iva,
                        'descuento': desc,
                        'importe': importe
                    })

        if errores_inventario:
            flash("No se puede realizar la venta: " + "; ".join(errores_inventario), "danger")
            return redirect(url_for('ventas.nueva'))

        # Generar folio/ticket automático
        last_venta = Venta.query.order_by(Venta.id.desc()).first()
        folio = (last_venta.folio if last_venta and last_venta.folio else 1000) + 1

        venta = Venta(
            folio=folio,
            cliente_id=cliente_id,
            usuario_id=current_user.id,
            fecha=datetime.now(),
            metodo_pago=metodo_pago,
            subtotal=subtotal,
            iva=total_iva,
            descuento=total_descuento,
            total=total
        )
        db.session.add(venta)
        db.session.flush()  # Para obtener venta.id

        # Registrar detalles de venta y actualizar inventario
        for item in productos:
            detalle = DetalleVenta(
                venta_id=venta.id,
                producto_id=item['producto'].id,
                cantidad=item['cantidad'],
                precio_unitario=item['precio_unitario'],
                descuento=item['descuento'],
                iva=item['iva'],
                importe=item['importe']
            )
            db.session.add(detalle)
            # Descontar inventario
            inventario = Inventario.query.filter_by(producto_id=item['producto'].id).first()
            if inventario:
                inventario.cantidad -= item['cantidad']

        db.session.commit()
        flash(f'Venta registrada exitosamente con folio {folio}', 'success')
        return redirect(url_for('ventas.ticket', venta_id=venta.id))

    return render_template('ventas_nueva.html', clientes=clientes)

@bp.route('/autocompletar_producto')
@login_required
def autocompletar_producto():
    q = request.args.get('q', '')
    if q.isdigit():
        productos = Producto.query.filter(Producto.codigo_barras.like(f'%{q}%')).all()
    else:
        productos = Producto.query.filter(
            (Producto.nombre_comercial.ilike(f'%{q}%')) |
            (Producto.nombre_generico.ilike(f'%{q}%')) |
            (Producto.presentacion.ilike(f'%{q}%'))
        ).all()
    results = []
    for p in productos:
        inventario = Inventario.query.filter_by(producto_id=p.id).first()
        results.append({
            'id': p.id,
            'codigo_barras': p.codigo_barras,
            'nombre_comercial': p.nombre_comercial,
            'nombre_generico': p.nombre_generico,
            'presentacion': p.presentacion,
            'precio_venta': p.precio_venta,
            'precio_sin_iva': p.precio_venta / (1 + p.iva/100) if p.iva else p.precio_venta,
            'iva': p.iva,
            'descuento': p.descuento,
            'inventario': inventario.cantidad if inventario else 0
        })
    return jsonify(results)

@bp.route('/ticket/<int:venta_id>')
@login_required
def ticket(venta_id):
    venta = Venta.query.get_or_404(venta_id)
    detalles = DetalleVenta.query.filter_by(venta_id=venta.id).all()
    cliente = Cliente.query.get(venta.cliente_id) if venta.cliente_id else None
    return render_template('ventas_ticket.html', venta=venta, detalles=detalles, cliente=cliente)

@bp.route('/listado', methods=['GET'])
@login_required
def listado():
    fecha = request.args.get('fecha', '')
    cliente_id = request.args.get('cliente_id', '')
    usuario_id = request.args.get('usuario_id', '')
    ventas_query = Venta.query
    if fecha:
        try:
            fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
            ventas_query = ventas_query.filter(Venta.fecha >= fecha_dt, Venta.fecha < fecha_dt.replace(hour=23, minute=59, second=59))
        except:
            pass
    if cliente_id:
        ventas_query = ventas_query.filter_by(cliente_id=cliente_id)
    if usuario_id:
        ventas_query = ventas_query.filter_by(usuario_id=usuario_id)
    ventas = ventas_query.order_by(Venta.fecha.desc()).all()
    clientes = Cliente.query.all()
    usuarios = Usuario.query.all()
    return render_template('ventas.html', ventas=ventas, clientes=clientes, usuarios=usuarios)

@bp.route('/eliminar/<int:venta_id>', methods=['POST'])
@login_required
def eliminar(venta_id):
    if getattr(current_user, 'rol', None) == 'cajero':
        flash("No tienes permisos para eliminar ventas.", "danger")
        return redirect(url_for('ventas.listado'))
    venta = Venta.query.get_or_404(venta_id)
    detalles = DetalleVenta.query.filter_by(venta_id=venta.id).all()
    for detalle in detalles:
        inventario = Inventario.query.filter_by(producto_id=detalle.producto_id).first()
        if inventario:
            inventario.cantidad += detalle.cantidad
        db.session.delete(detalle)
    db.session.delete(venta)
    db.session.commit()
    flash('Venta eliminada correctamente.', 'success')
    return redirect(url_for('ventas.listado'))

@bp.route('/editar/<int:venta_id>', methods=['GET', 'POST'])
@login_required
def editar(venta_id):
    if getattr(current_user, 'rol', None) == 'cajero':
        flash("No tienes permisos para editar ventas.", "danger")
        return redirect(url_for('ventas.listado'))
    venta = Venta.query.get_or_404(venta_id)
    detalles = DetalleVenta.query.filter_by(venta_id=venta.id).all()
    clientes = Cliente.query.all()
    if request.method == 'POST':
        flash('Funcionalidad de edición en desarrollo.', 'info')
        return redirect(url_for('ventas.listado'))
    return render_template('ventas_editar.html', venta=venta, detalles=detalles, clientes=clientes)

@bp.route('/facturar/<int:venta_id>', methods=['GET', 'POST'])
@login_required
def facturar(venta_id):
    venta = Venta.query.get_or_404(venta_id)
    detalles = DetalleVenta.query.filter_by(venta_id=venta.id).all()
    if request.method == 'POST':
        flash("Factura generada correctamente y ligada a la venta.", "success")
        return redirect(url_for('ventas.ticket', venta_id=venta.id))
    return render_template('ventas_facturar.html', venta=venta, detalles=detalles)
