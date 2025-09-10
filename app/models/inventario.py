from app.extensions import db
from datetime import datetime

class Inventario(db.Model):
    __tablename__ = 'inventario'
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    cantidad = db.Column(db.Integer, default=0)
    inventario_valor = db.Column(db.Float, default=0.0)
    punto_reorden = db.Column(db.Integer, default=0)
    cantidad_faltante = db.Column(db.Integer, default=0)
    fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    producto = db.relationship('Producto', backref='inventario')
