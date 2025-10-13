from app import create_app
from app.extensions import db
from app.models.usuario import Usuario

app = create_app()
with app.app_context():
    # Actualiza todos los roles incorrectos (cajero, caja, etc.) a "Caja"
    usuarios_caja = Usuario.query.filter(Usuario.rol.in_(["cajero", "caja"])).all()
    for usuario in usuarios_caja:
        usuario.rol = "Caja"
    db.session.commit()
    print(f"Se actualizaron {len(usuarios_caja)} usuarios a rol 'Caja'.")
