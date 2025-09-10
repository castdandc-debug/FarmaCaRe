from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.extensions import db
from app.models import Producto, Inventario

bp = Blueprint('productos', __name__, url_prefix='/productos')

@bp.route('/')
def lista():
    productos_db = Producto.query.filter_by(activo=True).all()
    productos = []
    for p in productos_db:
        descuento = p.descuento if p.descuento is not None else 0
        iva = p.iva if p.iva is not None else 0
        precio_sin_iva = round(p.precio_venta / (1 + iva/100), 2) if iva else p.precio_venta
        precio_venta = round(((p.precio_venta / (1 + iva/100)) * (1 - descuento/100)) * (1 + iva/100), 2) if iva else round(p.precio_venta * (1 - descuento/100), 2)
        productos.append({
            'id': p.id,
            'codigo_barras': p.codigo_barras,
            'nombre_comercial': p.nombre_comercial,
            'nombre_generico': p.nombre_generico if p.tipo == "medicamento" else p.nombre_comun,
            'presentacion': p.presentacion,
            'tipo': p.grupo if hasattr(p, 'grupo') and p.grupo else ("Medicamento" if p.tipo == "medicamento" else "Dispositivo Médico"),
            'tipo_slug': p.tipo,
            'precio_sin_iva': precio_sin_iva,
            'iva': iva,
            'descuento': descuento,
            'precio_venta': precio_venta
        })
    return render_template('productos.html', productos=productos)

@bp.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        tipo = request.form['tipo_producto']
        codigo_barras = request.form['codigo_barras']
        existe = Producto.query.filter_by(codigo_barras=codigo_barras).first()
        if existe:
            flash('Error: Ese código de barras ya existe en productos.', 'danger')
            return redirect(url_for('productos.agregar'))

        producto = Producto(
            codigo_barras=codigo_barras,
            nombre_comercial=request.form['nombre_comercial'],
            nombre_generico=request.form['nombre_generico'] if tipo == "medicamento" else None,
            nombre_comun=request.form['nombre_generico'] if tipo == "dispositivo" else None,
            laboratorio=request.form['laboratorio'],
            presentacion=request.form['presentacion'],
            grupo=request.form['grupo'] if tipo == "medicamento" else None,
            iva=float(request.form['iva']),
            descuento=float(request.form['descuento']),
            precio_venta=float(request.form['precio_venta']),
            activo=True,
            tipo=tipo
        )
        db.session.add(producto)
        db.session.commit()

        # Crear inventario para el nuevo producto con punto de reorden = 3 por defecto
        inventario = Inventario(
            producto_id=producto.id,
            producto_tipo=tipo,
            cantidad=0,  # Inicializa en 0
            punto_reorden=3
        )
        db.session.add(inventario)
        db.session.commit()

        flash('Producto agregado correctamente', 'success')
        return redirect(url_for('productos.lista'))
    return render_template('agregar_producto.html')

@bp.route('/editar/<tipo>/<int:id>', methods=['GET', 'POST'])
def editar(tipo, id):
    producto = Producto.query.filter_by(id=id, tipo=tipo).first_or_404()
    if request.method == 'POST':
        producto.codigo_barras = request.form['codigo_barras']
        producto.nombre_comercial = request.form['nombre_comercial']
        producto.laboratorio = request.form['laboratorio']
        producto.presentacion = request.form['presentacion']
        producto.iva = float(request.form['iva'])
        producto.descuento = float(request.form['descuento'])
        producto.precio_venta = float(request.form['precio_venta'])
        if tipo == "medicamento":
            producto.nombre_generico = request.form['nombre_generico']
            producto.grupo = request.form['grupo']
            producto.nombre_comun = None
        else:
            producto.nombre_comun = request.form['nombre_generico']
            producto.nombre_generico = None
            producto.grupo = None
        db.session.commit()
        flash('Producto actualizado correctamente', 'success')
        return redirect(url_for('productos.lista'))
    return render_template('editar_producto.html', producto=producto, tipo=tipo)

@bp.route('/eliminar/<tipo>/<int:id>', methods=['POST'])
def eliminar(tipo, id):
    producto = Producto.query.filter_by(id=id, tipo=tipo).first_or_404()
    inventario = Inventario.query.filter_by(producto_id=producto.id).first()
    if inventario and inventario.cantidad > 0:
        flash('No se puede eliminar el producto, tiene inventario vigente mayor a 0. Puede editarlo pero no eliminarlo.', 'danger')
        return redirect(url_for('productos.lista'))
    else:
        producto.activo = False
        db.session.commit()
        flash('Producto desactivado correctamente', 'success')
        return redirect(url_for('productos.lista'))
