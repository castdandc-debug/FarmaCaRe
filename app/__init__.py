# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from app.models import Usuario
    return Usuario.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'supersecretkey')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///farma.db')
    
    # Inicializar db con la aplicación
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Importar blueprints
    from app.views.auth import auth_bp
    from app.views.main import main_bp
    from app.modules.usuarios import usuarios_bp
    from app.modules.medicamentos import medicamentos_bp
    from app.modules.clientes import clientes_bp
    from app.modules.proveedores import proveedores_bp
    from app.modules.ventas import ventas_bp
    from app.modules.compras import compras_bp
    from app.modules.facturar import facturar_bp
    from app.modules.nohay import nohay_bp
    from app.modules.inventario import inventario_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(medicamentos_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(proveedores_bp)
    app.register_blueprint(ventas_bp)
    app.register_blueprint(compras_bp)
    app.register_blueprint(facturar_bp)
    app.register_blueprint(nohay_bp)
    app.register_blueprint(inventario_bp)

    return app
