# app/__init__.py
# -*- coding: utf-8 -*-
from flask import Flask
from .extensions import db, login_manager, bcrypt, migrate
import os
from sqlalchemy.exc import ProgrammingError

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'supersecretkey')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.login_view = 'auth.login'
    
    from .models import Usuario

    # Aquí se crea un contexto de la aplicación para interactuar con la base de datos
    with app.app_context():
        try:
            # Crea las tablas si no existen. Esto es redundante con flask db upgrade
            # pero sirve como una medida de seguridad.
            db.create_all()

            # Crea el usuario 'admin' si no existe
            if not Usuario.query.filter_by(nombre='admin').first():
                admin_password_hash = bcrypt.generate_password_hash('admin').decode('utf-8')
                admin_user = Usuario(
                    nombre='admin',
                    contraseña=admin_password_hash,
                    rol='admin'
                )
                db.session.add(admin_user)
                db.session.commit()
        except ProgrammingError as e:
            # Maneja el caso en que la tabla aún no se ha creado
            app.logger.error("Error al acceder a la tabla de usuarios: %s", e)
            # Reintenta el despliegue o la conexión

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

# Esta línea es la que necesita Gunicorn para encontrar tu app
app = create_app()
