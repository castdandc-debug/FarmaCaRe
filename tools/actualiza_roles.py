from app import create_app
from app.extensions import db
from app.models.usuario import Usuario

app = create_app()
with app.app_context():
    usuarios_cajero = Usuario.query.filter_by(rol="cajero").all()
    for usuario in usuarios_cajero:
        usuario.rol = "Caja"
    db.session.commit()
    print(f"Se actualizaron {len(usuarios_cajero)} usuarios a rol 'Caja'.")
