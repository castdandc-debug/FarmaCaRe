# -*- coding: utf-8 -*-
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    rol = db.Column(db.String(20), nullable=False, default='Caja')
    contraseña = db.Column(db.String(200), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        from werkzeug.security import generate_password_hash
        self.contraseña = generate_password_hash(password)

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.contraseña, password)

    def get_id(self):
        return str(self.id)


class Medicamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo_barras = db.Column(db.String(50), unique=True, nullable=False)
    nombre_comercial = db.Column(db.String(100), nullable=False)
    nombre_generico = db.Column(db.String(100))
    laboratorio = db.Column(db.String(100))
    presentacion = db.Column(db.String(50))
    grupo = db.Column(db.String(20))
    iva = db.Column(db.Float, default=0.0)
    precio_venta = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class DispositivoMedico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo_barras = db.Column(db.String(50), unique=True, nullable=False)
    nombre_comercial = db.Column(db.String(100), nullable=False)
    nombre_comun = db.Column(db.String(100))
    laboratorio = db.Column(db.String(100))
    presentacion = db.Column(db.String(50))
    iva = db.Column(db.Float, default=0.0)
    precio_venta = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    rfc = db.Column(db.String(20), unique=True)
    direccion = db.Column(db.String(200))
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(100))
    contacto = db.Column(db.String(100))
    telefono_contacto = db.Column(db.String(20))
    fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    rfc = db.Column(db.String(20), unique=True)
    direccion = db.Column(db.String(200))
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(100))
    contacto = db.Column(db.String(100))
    telefono_contacto = db.Column(db.String(20))
    fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class NoHay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50))
    descripcion = db.Column(db.Text)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)


class Entrada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    producto_id = db.Column(db.Integer)
    producto_tipo = db.Column(db.String(20))
    cantidad = db.Column(db.Integer, nullable=False)
    importe_unitario = db.Column(db.Float, nullable=False)
    importe_antes_iva = db.Column(db.Float)
    iva_porcentaje = db.Column(db.Float)
    valor_iva = db.Column(db.Float)
    importe_total = db.Column(db.Float)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'))
    compra_id = db.Column(db.Integer, db.ForeignKey('compra.id'), nullable=True)


class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_compra = db.Column(db.DateTime, default=datetime.utcnow)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)
    entradas = db.relationship('Entrada', backref='compra', lazy=True)


class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=True)
    total = db.Column(db.Float, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))


class Salida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    producto_id = db.Column(db.Integer)
    producto_tipo = db.Column(db.String(20))
    cantidad = db.Column(db.Integer, nullable=False)
    importe_unitario = db.Column(db.Float, nullable=False)
    importe_antes_iva = db.Column(db.Float)
    iva_porcentaje = db.Column(db.Float)
    valor_iva = db.Column(db.Float)
    importe_total = db.Column(db.Float)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=True)
    eliminada = db.Column(db.Boolean, default=False)


class Inventario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer)
    producto_tipo = db.Column(db.String(20))
    cantidad = db.Column(db.Integer, default=0)
    valor_inventario = db.Column(db.Float, default=0.0)
    punto_reorden = db.Column(db.Integer, default=10)
    cantidad_faltante = db.Column(db.Integer, default=0)
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class AjusteInventario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    producto_id = db.Column(db.Integer)
    producto_tipo = db.Column(db.String(20))
    cantidad_ajuste = db.Column(db.Integer, nullable=False)
    razon = db.Column(db.Text)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
