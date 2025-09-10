# -*- coding: utf-8 -*-
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from .extensions import db, login_manager, bcrypt, migrate
import os
from sqlalchemy.exc import ProgrammingError

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'supersecretkey')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.login_view = 'auth.login'
    
    # Importar modelos después de inicializar db
    from .models import Usuario

    with app.app_context():
        try:
            # Crear todas las tablas de la base de datos si no existen
            db.create_all()

            # Crear usuario admin si no existe
            if not Usuario.query.filter_by(nombre='admin').first():
                print("Creando usuario administrador...")
                admin = Usuario(nombre='admin', rol='Administrador')
                admin.set_password('admin')
                db.session.add(admin)
                db.session.commit()
                print("✅ Usuario admin creado exitosamente.")
            else:
                print("👤 Usuario admin ya existe.")
                
        except ProgrammingError as e:
            app.logger.error("Error al acceder a la tabla de usuarios: %s", e)

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    # Importar y registrar blueprints con las rutas correctas
    from .views.auth import auth_bp
    from .routes.main import main
    from .modules.core.users.usuarios import usuarios_bp
    # from .modules.inventory.products.medicamentos import medicamentos_bp
    from .modules.inventory.products.clientes import clientes_bp
    from .modules.inventory.products.proveedores import proveedores_bp

    # IMPORTA Y ALIAS LOS BLUEPRINTS PRINCIPALES COMO bp:
    from .modules.sales.ventas import bp as ventas_bp
    from .modules.sales.compras import bp as compras_bp
    from .modules.sales.facturar import bp as facturar_bp
    from .modules.nohay import bp as nohay_bp
    from .modules.inventory.products.inventario import bp as inventario_bp
    # from .modules.inventory.products.dispositivos import bp as dispositivos_bp
    from .modules.inventory.products.productos import bp as productos_bp
    from app.modules.reportes.informe import bp as informe_bp

    # Registrar blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main)
    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
    # app.register_blueprint(medicamentos_bp, url_prefix='/medicamentos')
    app.register_blueprint(clientes_bp, url_prefix='/clientes')
    app.register_blueprint(proveedores_bp, url_prefix='/proveedores')
    app.register_blueprint(ventas_bp, url_prefix='/ventas')
    app.register_blueprint(compras_bp, url_prefix='/compras')
    app.register_blueprint(facturar_bp, url_prefix='/facturar')
    app.register_blueprint(nohay_bp, url_prefix='/nohay')
    app.register_blueprint(inventario_bp, url_prefix='/inventario')
    # app.register_blueprint(dispositivos_bp, url_prefix='/dispositivos')
    app.register_blueprint(productos_bp, url_prefix='/productos')
    app.register_blueprint(informe_bp)

    return app

# Esta línea es la que necesita Gunicorn para encontrar tu app
app = create_app()
