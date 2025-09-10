from app.extensions import db

class DetalleCompra(db.Model):
    __tablename__ = 'detalle_compra'
    id = db.Column(db.Integer, primary_key=True)
    compra_id = db.Column(db.Integer, db.ForeignKey('compras.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    precio_sin_iva = db.Column(db.Float, nullable=False)
    importe = db.Column(db.Float, nullable=False)
    descuento = db.Column(db.Float, nullable=False, default=0.0)
    iva = db.Column(db.Float, nullable=False, default=16.0)

    compra = db.relationship('Compra', backref='detalles')
    producto = db.relationship('Producto', backref='detalles_compra')

    def __repr__(self):
        return f'<DetalleCompra compra {self.compra_id} producto {self.producto_id}>'
