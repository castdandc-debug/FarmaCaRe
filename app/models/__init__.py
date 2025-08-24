# -*- coding: utf-8 -*-
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# La instancia db viene de app/__init__.py
from app import db

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    rol = db.Column(db.String(20), default='usuario')
    created_at = db.Column(db.DateTime, default=datetime.now)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f'<Usuario {self.username}>'


class Medicamento(db.Model):
    __tablename__ = 'medicamentos'

    id = db.Column(db.Integer, primary_key=True)
    codigo_barras = db.Column(db.String(50), unique=True, nullable=False)
    nombre_comercial = db.Column(db.String(100), nullable=False)
    nombre_generico = db.Column(db.String(100))
    laboratorio = db.Column(db.String(100), nullable=False)
    presentacion = db.Column(db.String(100), nullable=False)
    grupo = db.Column(db.String(20), nullable=False)
    iva = db.Column(db.Float, default=0.0)
    precio_venta = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Medicamento {self.nombre_comercial}>'
