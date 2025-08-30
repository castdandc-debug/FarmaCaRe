# app/models.py
from app.extensions import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Modelo de Usuario
class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    contraseña = db.Column(db.String(128), nullable=False)
    rol = db.Column(db.String(20), nullable=False, default='Caja')
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def set_password(self, password):
        self.contraseña = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.contraseña, password)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'

# Modelo de Cliente
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    rfc = db.Column(db.String(13), nullable=True)
    direccion = db.Column(db.String(200), nullable=True)
    telefono = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    contacto = db.Column(db.String(150), nullable=True)
    telefono_contacto = db.Column(db.String(15), nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Cliente {self.nombre}>'

# Modelo de Proveedor
class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    rfc = db.Column(db.String(13), nullable=True)
    direccion = db.Column(db.String(200), nullable=True)
    telefono = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    contacto = db.Column(db.String(150), nullable=True)
    telefono_contacto = db.Column(db.String(15), nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Proveedor {self.nombre}>'

# Modelo de Medicamento
class Medicamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo_barras = db.Column(db.String(50), unique=True, nullable=False)
    nombre_comercial = db.Column(db.String(150), nullable=False)
    nombre_generico = db.Column(db.String(150), nullable=False)
    laboratorio = db.Column(db.String(100), nullable=False)
    presentacion = db.Column(db.String(100), nullable=False)
    grupo = db.Column(db.String(20), nullable=False)  # I, II, III, IV, V, IV-Antibiótico
    iva = db.Column(db.Float, default=0.0)  # Porcentaje de IVA
    precio_venta = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    punto_reorden = db.Column(db.Integer, default=10)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Medicamento {self.nombre_comercial}>'

# Modelo de No Hay
class NoHay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # 'Poco inventario', 'No tiene el proveedor', 'Descontinuado', 'No existe'
    descripcion = db.Column(db.Text, nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<NoHay {self.nombre}>'

# Modelo de Salida (para compatibilidad con facturar.py)
class Salida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    producto_id = db.Column(db.Integer, nullable=False)
    producto_tipo = db.Column(db.String(20), nullable=False)  # 'Medicamento' o 'DispositivoMedico'
    cantidad = db.Column(db.Integer, nullable=False)
    importe_unitario = db.Column(db.Float, nullable=False)
    importe_antes_iva = db.Column(db.Float, nullable=False)
    iva_porcentaje = db.Column(db.Float, default=0.0)
    valor_iva = db.Column(db.Float, default=0.0)
    importe_total = db.Column(db.Float, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    eliminada = db.Column(db.Boolean, default=False)
    
    cliente = db.relationship('Cliente', backref='salidas')
    usuario = db.relationship('Usuario', backref='salidas')

    def __repr__(self):
        return f'<Salida {self.fecha}>'

# Modelos heredados para compatibilidad
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(250))
    stock = db.Column(db.Integer, default=0)
    precio = db.Column(db.Float, nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'))
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    proveedor = db.relationship('Proveedor', backref='productos_genericos')

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    total = db.Column(db.Float, default=0.0)
    
    cliente = db.relationship('Cliente', backref='ventas_legacy')
    usuario = db.relationship('Usuario', backref='ventas_legacy')

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    total = db.Column(db.Float, default=0.0)
    
    proveedor = db.relationship('Proveedor', backref='compras_legacy')
    usuario = db.relationship('Usuario', backref='compras_legacy')
