from app.extensions import db
from datetime import datetime

class AjusteInventario(db.Model):
    __tablename__ = 'ajustes_inventario'
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    cantidad_ajustada = db.Column(db.Integer, nullable=False)
    motivo = db.Column(db.String(255))
    fecha_ajuste = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    producto = db.relationship('Producto', backref='ajustes_inventario')
    usuario = db.relationship('Usuario', backref='ajustes_inventario')
