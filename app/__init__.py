# -*- coding: utf-8 -*-
from flask import Flask
from .extensions import db, login_manager, bcrypt, migrate
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'supersecretkey')
    # Este es el cambio clave para usar la variable de entorno de Render
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar las extensiones aquí
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.login_view = 'auth.login'
    
    # Importar los modelos para que la app los reconozca
    from .models import Usuario

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    # Importar y registrar blueprints
    from .views.auth import auth_bp
    from .routes.main import main
    from .modules.usuarios import usuarios_bp
    from .modules.medicamentos import medicamentos_bp
    from .modules.clientes import clientes_bp
    from .modules.proveedores import proveedores_bp
    from .modules.ventas import ventas_bp
    from .modules.compras import compras_bp
    from .modules.facturar import facturar_bp
    from .modules.nohay import nohay_bp
    from .modules.inventario import inventario_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main)
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
