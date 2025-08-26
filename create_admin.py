# create_admin.py
from app import create_app
from app.models import db, Usuario
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # ✅ Crear tablas si no existen
    db.create_all()
    print("Tablas creadas exitosamente.")

    # ✅ Verificar si el usuario admin ya existe
    if not Usuario.query.filter_by(nombre='admin').first():
        admin = Usuario(
            nombre='admin',
            rol='Administrador',
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print("✅ Usuario 'admin' creado con éxito.")
    else:
        print("👤 El usuario 'admin' ya existe.")
