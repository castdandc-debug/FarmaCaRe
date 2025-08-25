# run.py
import os
from app import create_app
from app.models import db, Usuario

# Crear e inicializar la aplicación Flask
app = create_app()

if __name__ == '__main__':
    # Usar el contexto de la aplicación para interactuar con la base de datos
    with app.app_context():
        # Crear todas las tablas de la base de datos si no existen
        db.create_all()

        # Crear usuario admin si no existe
        if not Usuario.query.filter_by(nombre='admin').first():
            print("Creando usuario administrador...")
            admin = Usuario(nombre='admin', rol='Administrador')
            admin.set_password('123456') # Considera cambiar esta contraseña por una más segura
            db.session.add(admin)
            db.session.commit()
            print("✅ Usuario admin creado exitosamente.")
        else:
            print("👤 Usuario admin ya existe.")

    # Obtener el puerto desde la variable de entorno de Render o usar el puerto 10000 por defecto
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
