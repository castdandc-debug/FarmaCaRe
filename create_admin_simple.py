# create_admin_simple.py
from app import create_app
from app.models import db, Usuario
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Crear tablas si no existen
    db.create_all()
    print("Tablas creadas exitosamente.")

    # Eliminar usuario anterior (si existe)
    if Usuario.query.filter_by(nombre='admin').first():
        db.session.delete(Usuario.query.filter_by(nombre='admin').first())
        db.session.commit()
        print("Usuario anterior eliminado.")

    # Crear nuevo usuario con contraseña simple
    admin = Usuario(
        nombre='admin',
        rol='Administrador'
    )
    admin.set_password('123456')  # Contraseña simple sin caracteres especiales
    db.session.add(admin)
    db.session.commit()
    print("✅ Usuario 'admin' creado con éxito.")
