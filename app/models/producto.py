from app.extensions import db
from datetime import datetime

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)
    codigo_barras = db.Column(db.String(50), unique=True, nullable=False)
    nombre_comercial = db.Column(db.String(150), nullable=False)
    nombre_generico = db.Column(db.String(150), nullable=True)
    nombre_comun = db.Column(db.String(150), nullable=True)
    laboratorio = db.Column(db.String(100), nullable=True)
    presentacion = db.Column(db.String(100), nullable=True)
    grupo = db.Column(db.String(50), nullable=True)
    iva = db.Column(db.Float, default=0.0)
    descuento = db.Column(db.Float, default=0.0)
    precio_venta = db.Column(db.Float, nullable=False)
    punto_reorden = db.Column(db.Integer, default=10)
    activo = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'), nullable=True)

    proveedor = db.relationship('Proveedor', backref='productos')

    def __repr__(self):
        return f'<Producto {self.nombre_comercial} ({self.tipo})>'
