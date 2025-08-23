# -*- coding: utf-8 -*-
from datetime import datetime
from app import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Medicamento(BaseModel):
    __tablename__ = 'medicamentos'
    codigo_barras = db.Column(db.String(50), unique=True, nullable=False)
    nombre_comercial = db.Column(db.String(100), nullable=False)
    nombre_generico = db.Column(db.String(100))
    laboratorio = db.Column(db.String(100))
    presentacion = db.Column(db.String(50))
    grupo = db.Column(db.String(20))
    iva = db.Column(db.Float, default=0.0)
    precio_venta = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Medicamento {self.nombre_comercial}>"


class Usuario(BaseModel):
    __tablename__ = 'usuarios'
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    rol = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.username} - {self.rol}>"

    # Métodos requeridos por Flask-Login
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
