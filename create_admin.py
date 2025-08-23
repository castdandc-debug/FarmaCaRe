from app import create_app
from app.models import db, Usuario
from werkzeug.security import generate_password_hash

app = create_app()
app.app_context().push()

if not Usuario.query.filter_by(username="admin").first():
    admin = Usuario(
        username="admin",
        password_hash=generate_password_hash("admin123"),
        rol="administrador"
    )
    db.session.add(admin)
    db.session.commit()
    print("✅ Usuario 'admin' creado con éxito")
else:
    print("👤 Usuario 'admin' ya existe")
