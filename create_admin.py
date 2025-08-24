# -*- coding: utf-8 -*-
from app import create_app, db
from app.models import Usuario
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.create_all()  # Asegura que las tablas existan

    # Verifica si el admin ya existe
    admin = Usuario.query.filter_by(nombre='admin').first()
    if not admin:
        admin = Usuario(
            nombre='admin',
            rol='Admin',
            contraseña=generate_password_hash('admin123')
        )
        db.session.add(admin)
        db.session.commit()
        print("Administrador creado con éxito.")
    else:
        print("El administrador ya existe.")
