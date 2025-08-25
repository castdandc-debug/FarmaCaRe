# -*- coding: utf-8 -*-
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db

# Definición del modelo de Usuario
class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    rol = db.Column(db.String(20), nullable=False, default='Caja')
    contraseña = db.Column(db.String(200), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.contraseña = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.contraseña, password)

    def get_id(self):
        return str(self.id)

# Definición del modelo de Cliente
class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    rfc = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15))
    direccion = db.Column(db.String(200))

# Definición del modelo de Medicamento
class Medicamento(db.Model):
    __tablename__ = 'medicamentos'
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

# Definición del modelo de Dispositivo Médico
class DispositivoMedico(db.Model):
    __tablename__ = 'dispositivos_medicos'
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

# Definición del modelo de Proveedor
class Proveedor(db.Model):
    __tablename__ = 'proveedores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    rfc = db.Column(db.String(20), unique=True)
    direccion = db.Column(db.String(200))
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(100))

# Definición del modelo de Venta (Nota de Venta)
class Venta(db.Model):
    __tablename__ = 'ventas'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=True)
    total = db.Column(db.Float, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

# Definición del modelo de Compra (Ingreso de Factura)
class Compra(db.Model):
    __tablename__ = 'compras'
    id = db.Column(db.Integer, primary_key=True)
    fecha_compra = db.Column(db.DateTime, default=datetime.utcnow)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

# Definición del modelo de Entradas
class Entrada(db.Model):
    __tablename__ = 'entradas'
    id = db.Column(db.Integer, primary_key=True)
    compra_id = db.Column(db.Integer, db.ForeignKey('compras.id'))
    producto_id = db.Column(db.Integer) # Para Medicamentos/Dispositivos
    tipo_producto = db.Column(db.String(20)) # 'medicamento' o 'dispositivo'
    cantidad = db.Column(db.Integer, nullable=False)
    importe_unitario = db.Column(db.Float, nullable=False)
    importe_antes_iva = db.Column(db.Float, nullable=False)
    iva_porcentaje = db.Column(db.Float, nullable=False)
    valor_iva = db.Column(db.Float, nullable=False)
    importe_total = db.Column(db.Float, nullable=False)

# Definición del modelo de Salidas
class Salida(db.Model):
    __tablename__ = 'salidas'
    id = db.Column(db.Integer, primary_key=True)
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'))
    producto_id = db.Column(db.Integer) # Para Medicamentos/Dispositivos
    tipo_producto = db.Column(db.String(20)) # 'medicamento' o 'dispositivo'
    cantidad = db.Column(db.Integer, nullable=False)
    importe_unitario = db.Column(db.Float, nullable=False)
    importe_antes_iva = db.Column(db.Float, nullable=False)
    iva_porcentaje = db.Column(db.Float, nullable=False)
    valor_iva = db.Column(db.Float, nullable=False)
    importe_total = db.Column(db.Float, nullable=False)

# Definición del modelo de Inventario
class Inventario(db.Model):
    __tablename__ = 'inventario'
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer) # Para Medicamentos/Dispositivos
    tipo_producto = db.Column(db.String(20)) # 'medicamento' o 'dispositivo'
    cantidad = db.Column(db.Integer, default=0)
    inventario_valor = db.Column(db.Float, default=0.0)
    punto_reorden = db.Column(db.Integer, default=0)
    cantidad_faltante = db.Column(db.Integer, default=0)
    fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Definición del modelo de NoHay
class NoHay(db.Model):
    __tablename__ = 'no_hay'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50)) # 'Poco inventario', 'No tiene el proveedor', etc.
    descripcion = db.Column(db.String(255))
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

# Definición del modelo de Ajuste de Inventario
class AjusteInventario(db.Model):
    __tablename__ = 'ajustes_inventario'
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer)
    tipo_producto = db.Column(db.String(20))
    cantidad_ajustada = db.Column(db.Integer, nullable=False)
    motivo = db.Column(db.String(255))
    fecha_ajuste = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
