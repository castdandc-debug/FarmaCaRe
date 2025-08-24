# -*- coding: utf-8 -*-
from app import create_app, db
from app.models import Usuario

app = create_app()

with app.app_context():
    db.create_all()
    
    admin = Usuario(
        username='admin',
        rol='administrador'
    )
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()

    print("Administrador creado con éxito.")
