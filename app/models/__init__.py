# -*- coding: utf-8 -*-
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Usuario(UserMixin):
    def __init__(self, id=None, username=None, password=None, rol=None):
        self.id = id
        self.username = username
        self.password = password
        self.rol = rol or 'usuario'
        self.created_at = datetime.now()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<Usuario {self.username}>'
