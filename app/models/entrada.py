from app.extensions import db

class Entrada(db.Model):
    __tablename__ = 'entradas'
    id = db.Column(db.Integer, primary_key=True)
    compra_id = db.Column(db.Integer, db.ForeignKey('compras.id'))
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    cantidad = db.Column(db.Integer, nullable=False)
    importe_unitario = db.Column(db.Float, nullable=False)
    importe_antes_iva = db.Column(db.Float, nullable=False)
    iva_porcentaje = db.Column(db.Float, nullable=False)
    valor_iva = db.Column(db.Float, nullable=False)
    importe_total = db.Column(db.Float, nullable=False)

    compra = db.relationship('Compra', backref='entradas')
    producto = db.relationship('Producto', backref='entradas')
