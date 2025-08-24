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

    # Inicializa db con la app
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Registrar blueprints
    from app.views.auth import auth_bp
    from app.views.main import main_bp
    from app.modules.medicamentos import medicamentos_bp
    from app.modules.usuarios import usuarios_bp  # ✅ Importar usuarios_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(medicamentos_bp)
    app.register_blueprint(usuarios_bp)  # ✅ Registrar usuarios_bp

    return app
