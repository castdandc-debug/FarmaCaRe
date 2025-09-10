from app.extensions import db
from datetime import datetime

class Compra(db.Model):
    __tablename__ = 'compras'
    id = db.Column(db.Integer, primary_key=True)
    fecha_compra = db.Column(db.DateTime, default=datetime.utcnow)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'), nullable=False)
    total = db.Column(db.Float, nullable=False, default=0.0)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    folio_factura = db.Column(db.String(100), nullable=True)

    proveedor = db.relationship('Proveedor', backref='compras')
    usuario = db.relationship('Usuario', backref='compras')
