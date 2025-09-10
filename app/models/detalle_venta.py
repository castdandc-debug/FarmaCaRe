from app.extensions import db

class DetalleVenta(db.Model):
    __tablename__ = 'detalles_venta'
    id = db.Column(db.Integer, primary_key=True)
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    descuento = db.Column(db.Float, default=0.0)
    iva = db.Column(db.Float, default=0.0)
    importe = db.Column(db.Float, nullable=False)  # Calculado: (precio_unitario * cantidad + iva - descuento)
    
    venta = db.relationship('Venta', backref='detalles')
    producto = db.relationship('Producto', backref='detalles_venta')
