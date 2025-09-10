from app.extensions import db
from datetime import datetime

class Salida(db.Model):
    __tablename__ = 'salidas'
    id = db.Column(db.Integer, primary_key=True)
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'), nullable=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    importe_unitario = db.Column(db.Float, nullable=False)
    importe_antes_iva = db.Column(db.Float, nullable=False)
    iva_porcentaje = db.Column(db.Float, default=0.0)
    valor_iva = db.Column(db.Float, default=0.0)
    importe_total = db.Column(db.Float, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    eliminada = db.Column(db.Boolean, default=False)

    cliente = db.relationship('Cliente', backref='salidas')
    usuario = db.relationship('Usuario', backref='salidas')
    producto = db.relationship('Producto', backref='salidas')
    venta = db.relationship('Venta', backref='salidas')

    def __repr__(self):
        return f'<Salida {self.fecha}>'
