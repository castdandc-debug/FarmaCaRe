from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from app.extensions import db
from app.models import (
    Producto, Inventario, DetalleCompra, DetalleVenta, Venta, Compra,
    CierreCaja, Usuario, AjusteInventario, NoHay,
    Entrada, Salida
)
from datetime import datetime

bp = Blueprint('informe', __name__, url_prefix='/reportes/informe')

# 1. Informe general (solo administrador)
@bp.route('/', methods=['GET', 'POST'])
@login_required
def informe_general():
    if getattr(current_user, "rol", "") != "Administrador":
        abort(403)

    busqueda = request.args.get('busqueda', '').strip()
    query = Producto.query
    if busqueda:
        query = query.filter(Producto.nombre_comercial.ilike(f'%{busqueda}%'))

    productos = query.all()
    productos_data = []

    for p in productos:
        inv = Inventario.query.filter_by(producto_id=p.id).first()
        detalles = DetalleCompra.query.filter_by(producto_id=p.id).all()
        cantidad_actual = inv.cantidad if inv else 0
        total_costo = sum(d.precio_unitario * d.cantidad for d in detalles)
        total_cantidad = sum(d.cantidad for d in detalles)
        costo_promedio = (total_costo / total_cantidad) if total_cantidad > 0 else 0
        margen = (p.precio_venta - costo_promedio) if p.precio_venta else 0

        productos_data.append({
            'id': p.id,
            'nombre_comercial': p.nombre_comercial,
            'precio_venta': p.precio_venta,
            'costo': costo_promedio,
            'margen': margen,
            'cantidad': cantidad_actual
        })

    total_compras = db.session.query(db.func.sum(Compra.total)).scalar() or 0
    total_ventas = db.session.query(db.func.sum(Venta.total)).scalar() or 0
    cierres = CierreCaja.query.order_by(CierreCaja.fecha.desc()).all()

    return render_template(
        'reportes/informe.html',
        productos=productos_data,
        total_compras=total_compras,
        total_ventas=total_ventas,
        cierres=cierres,
        busqueda=busqueda
    )

@bp.route('/editar_cierre/<int:id>', methods=['POST'])
@login_required
def editar_cierre(id):
    if getattr(current_user, "rol", "") != "Administrador":
        abort(403)
    cierre = CierreCaja.query.get_or_404(id)
    cierre.faltante = request.form.get('faltante', cierre.faltante)
    cierre.entregado = request.form.get('entregado', cierre.entregado)
    db.session.commit()
    flash("Cierre de caja actualizado correctamente.", "success")
    return redirect(url_for('informe.informe_general'))

# 2. Cortes de caja (caja + administrador, arqueo con divisas mexicanas)
@bp.route('/cortes_caja', methods=['GET', 'POST'])
@login_required
def cortes_caja():
    if getattr(current_user, "rol", "") not in ["Administrador", "Caja"]:
        abort(403)

    usuario_id = request.args.get('usuario_id') or current_user.id
    fecha = request.args.get('fecha')
    query = CierreCaja.query
    if usuario_id:
        query = query.filter_by(usuario_id=usuario_id)
    if fecha:
        try:
            fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
            query = query.filter(db.func.date(CierreCaja.fecha) == fecha_dt.date())
        except ValueError:
            pass
    cortes = query.order_by(CierreCaja.fecha.desc()).all()

    # Lógica para obtener ventas del usuario menos lo entregado en cierres anteriores
    ventas_totales = db.session.query(db.func.sum(Venta.total)).filter(Venta.usuario_id == usuario_id).scalar() or 0
    entregado_total = db.session.query(db.func.sum(CierreCaja.corte_entregado)).filter(CierreCaja.usuario_id == usuario_id).scalar() or 0
    venta_pendiente_usuario = ventas_totales - entregado_total

    return render_template(
        'reportes/cortes_caja.html',
        cortes=cortes,
        total_ventas_usuario=venta_pendiente_usuario
    )

# 2b. Guardar cierre de caja - POST (DEBES AGREGAR EN TU FRONT EL FORM PARA ENVIAR ESTOS DATOS)
@bp.route('/guardar_cierre', methods=['POST'])
@login_required
def guardar_cierre():
    if getattr(current_user, "rol", "") not in ["Administrador", "Caja"]:
        abort(403)

    # Recoge los datos del arqueo
    corte_entregado = float(request.form.get('corte_entregado', 0))
    faltante = float(request.form.get('faltante', 0))
    entregado = float(request.form.get('total_ventas_usuario', 0))
    usuario_id = current_user.id

    cierre = CierreCaja(
        fecha=datetime.utcnow(),
        usuario_id=usuario_id,
        corte_entregado=corte_entregado,
        faltante=faltante,
        entregado=entregado
    )
    db.session.add(cierre)
    db.session.commit()
    flash("Corte de caja registrado correctamente.", "success")
    return redirect(url_for('informe.cortes_caja'))

# 3. Ajustes de inventario (solo administrador)
@bp.route('/ajustes_inventario', methods=['GET', 'POST'])
@login_required
def ajustes_inventario():
    if getattr(current_user, "rol", "") != "Administrador":
        abort(403)

    busqueda = request.args.get('busqueda', '').strip()
    query = Producto.query
    if busqueda:
        query = query.filter(
            db.or_(
                Producto.nombre_comercial.ilike(f'%{busqueda}%'),
                Producto.nombre_generico.ilike(f'%{busqueda}%'),
                Producto.codigo_barras.ilike(f'%{busqueda}%')
            )
        )
    productos = query.all()

    # Diccionario para datos actuales por producto_id
    datos_actuales = {}
    for p in productos:
        inv = Inventario.query.filter_by(producto_id=p.id).first()
        datos_actuales[p.id] = {
            "inventario": inv.cantidad if inv else 0,
            "punto_reorden": inv.punto_reorden if inv else 0
        }

    # Procesar el ajuste POST
    if request.method == 'POST':
        producto_id = request.form.get('producto_id')
        tipo_ajuste = request.form.get('tipo_ajuste')
        cantidad = int(request.form.get('cantidad', 0))

        producto = Producto.query.get(producto_id)
        inv = Inventario.query.filter_by(producto_id=producto_id).first()

        if producto and inv:
            if tipo_ajuste == "entrada":
                ajuste = AjusteInventario(
                    producto_id=producto.id,
                    cantidad_ajustada=cantidad,
                    motivo=f"Entrada por ajuste",
                    usuario_id=current_user.id
                )
                inv.cantidad += cantidad
                db.session.add(ajuste)
                db.session.commit()
                flash("Entrada registrada correctamente.", "success")
            elif tipo_ajuste == "salida":
                ajuste = AjusteInventario(
                    producto_id=producto.id,
                    cantidad_ajustada=-cantidad,
                    motivo=f"Salida por ajuste",
                    usuario_id=current_user.id
                )
                inv.cantidad -= cantidad
                db.session.add(ajuste)
                db.session.commit()
                flash("Salida registrada correctamente.", "success")
            elif tipo_ajuste == "reorden":
                inv.punto_reorden = cantidad
                db.session.commit()
                flash("Punto de reorden actualizado.", "success")
        else:
            flash("Producto no encontrado o sin inventario.", "danger")

    return render_template(
        'reportes/ajustes_inventario.html',
        productos=productos,
        datos_actuales=datos_actuales,
        busqueda=busqueda
    )

# 4. Kardex (caja + administrador)
@bp.route('/kardex', methods=['GET'])
@login_required
def kardex():
    if getattr(current_user, "rol", "") not in ["Administrador", "Caja"]:
        abort(403)
    producto_busqueda = request.args.get('producto', '').strip()
    producto = None
    inventario = None
    movimientos = []

    # Sugerencias para el buscador: nombre comercial, código, genérico
    productos_sugerencias = Producto.query.filter_by(activo=True).order_by(Producto.nombre_comercial.asc()).all()

    if producto_busqueda:
        producto = Producto.query.filter(
            db.or_(
                Producto.nombre_comercial.ilike(f'%{producto_busqueda}%'),
                Producto.nombre_generico.ilike(f'%{producto_busqueda}%'),
                Producto.codigo_barras.ilike(f'%{producto_busqueda}%')
            )
        ).first()

        if producto:
            inventario = Inventario.query.filter_by(producto_id=producto.id).first()

            # 1. COMPRA/ENTRADA (del proveedor)
            detalles_compra = DetalleCompra.query.filter_by(producto_id=producto.id).all()
            for dc in detalles_compra:
                movimientos.append({
                    'fecha': dc.compra.fecha_compra if dc.compra else None,
                    'tipo': 'Compra',
                    'cantidad': dc.cantidad,
                    'usuario': dc.compra.usuario.nombre if dc.compra and dc.compra.usuario else '',
                })

            # 2. AJUSTES DE INVENTARIO
            ajustes = AjusteInventario.query.filter_by(producto_id=producto.id).all()
            for a in ajustes:
                tipo = 'Entrada por ajuste' if a.cantidad_ajustada > 0 else 'Salida por ajuste'
                movimientos.append({
                    'fecha': a.fecha_ajuste,
                    'tipo': tipo,
                    'cantidad': abs(a.cantidad_ajustada),
                    'usuario': a.usuario.nombre if a.usuario else '',
                })

            # 3. VENTA (DetalleVenta)
            detalles_venta = DetalleVenta.query.filter_by(producto_id=producto.id).all()
            for dv in detalles_venta:
                movimientos.append({
                    'fecha': dv.venta.fecha if dv.venta else None,
                    'tipo': 'Venta',
                    'cantidad': dv.cantidad,
                    'usuario': dv.venta.usuario.nombre if dv.venta and dv.venta.usuario else '',
                })

            # 4. SALIDA DIRECTA
            salidas = Salida.query.filter_by(producto_id=producto.id).all()
            for s in salidas:
                # Si está ligada a venta ya la contamos arriba, solo cuenta salidas directas
                if not s.venta_id:
                    movimientos.append({
                        'fecha': s.fecha,
                        'tipo': 'Salida',
                        'cantidad': s.cantidad,
                        'usuario': s.usuario.nombre if s.usuario else '',
                    })

            # 5. ENTRADAS (por Entrada, si tienes registros de entrada distintos a compra)
            entradas = Entrada.query.filter_by(producto_id=producto.id).all()
            for e in entradas:
                movimientos.append({
                    'fecha': e.compra.fecha_compra if e.compra else None,
                    'tipo': 'Entrada',
                    'cantidad': e.cantidad,
                    'usuario': e.compra.usuario.nombre if e.compra and e.compra.usuario else '',
                })

            # Ordenar movimientos por fecha DESC (más reciente primero)
            movimientos.sort(key=lambda x: x['fecha'] if x['fecha'] else datetime.min, reverse=True)

    return render_template(
        'reportes/kardex.html',
        producto=producto,
        inventario=inventario,
        movimientos=movimientos,
        productos_sugerencias=productos_sugerencias,
        busqueda=producto_busqueda
    )

# 5. No hay (solo administrador)
@bp.route('/no_hay', methods=['GET', 'POST'])
@login_required
def no_hay():
    if getattr(current_user, "rol", "") != "Administrador":
        abort(403)

    # Edición de registro
    if request.method == 'POST':
        if request.form.get('edit_id'):  # Edición existente
            nohay_id = request.form.get('edit_id')
            tipo = request.form.get('edit_tipo', '')
            descripcion = request.form.get('edit_descripcion', '')
            producto_no_hay = NoHay.query.get(nohay_id)
            if producto_no_hay:
                producto_no_hay.tipo = tipo
                producto_no_hay.descripcion = descripcion
                producto_no_hay.fecha_modificacion = datetime.utcnow()
                db.session.commit()
                flash("Registro actualizado correctamente.", "success")
            else:
                flash("Registro no encontrado.", "danger")
        else:  # Alta nueva
            nombre = request.form.get('nombre')
            tipo = request.form.get('tipo', '')
            descripcion = request.form.get('descripcion', '')
            producto_no_hay = NoHay(
                nombre=nombre,
                tipo=tipo,
                descripcion=descripcion,
                usuario_id=current_user.id
            )
            db.session.add(producto_no_hay)
            db.session.commit()
            flash("Producto agregado a 'No Hay'.", "success")

    # Filtro para incompletos
    filtrar_incompletos = request.args.get('incompletos', '0') == '1'
    query = NoHay.query
    if filtrar_incompletos:
        query = query.filter(
            (NoHay.tipo == '') | (NoHay.tipo == None) | 
            (NoHay.descripcion == '') | (NoHay.descripcion == None)
        )
    productos_no_hay = query.order_by(NoHay.fecha_creacion.desc()).all()

    return render_template(
        'reportes/no_hay.html',
        productos_no_hay=productos_no_hay,
        filtrar_incompletos=filtrar_incompletos
    )
