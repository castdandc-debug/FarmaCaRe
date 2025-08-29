import os
from werkzeug.security import generate_password_hash
from app import create_app
from app.models import Usuario
from app.extensions import db

# Importar y configurar la aplicación
app = create_app()

with app.app_context():
    print("Buscando usuario 'admin'...")
    admin_user = Usuario.query.filter_by(nombre='admin').first()

    if admin_user:
        # Generar el hash de la nueva contraseña
        new_password_hash = generate_password_hash('admin')

        # Actualizar el campo de contraseña en el usuario 'admin'
        admin_user.contraseña = new_password_hash
        db.session.commit()
        print("¡Contraseña de 'admin' actualizada exitosamente!")
    else:
        print("No se encontró el usuario 'admin'.")
