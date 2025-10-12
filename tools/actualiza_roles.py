from app import create_app
from app.extensions import db
from app.models.usuario import Usuario

app = create_app()
with app.app_context():
    usuarios_caja = Usuario.query.filter_by(rol="caja").all()
    for usuario in usuarios_cajero:
        usuario.rol = "Caja"
    db.session.commit()
    print(f"Se actualizaron {len(usuarios_caja)} usuarios a rol 'Caja'.")
