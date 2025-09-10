from app.extensions import db
from datetime import datetime

class Venta(db.Model):
    __tablename__ = 'ventas'
    id = db.Column(db.Integer, primary_key=True)
    folio = db.Column(db.Integer, unique=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=True)
    subtotal = db.Column(db.Float, nullable=True, default=0.0)
    iva = db.Column(db.Float, nullable=True, default=0.0)
    descuento = db.Column(db.Float, nullable=True, default=0.0)    # <-- CAMPO AGREGADO
    total = db.Column(db.Float, nullable=False, default=0.0)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    metodo_pago = db.Column(db.String(50), nullable=True)

    cliente = db.relationship('Cliente', backref='ventas')
    usuario = db.relationship('Usuario', backref='ventas')
