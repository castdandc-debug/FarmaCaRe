from app.extensions import db
from datetime import datetime

class CierreCaja(db.Model):
    __tablename__ = 'cierres_caja'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    corte_entregado = db.Column(db.Float, nullable=False)
    faltante = db.Column(db.Float, nullable=False, default=0.0)
    entregado = db.Column(db.Float, nullable=False, default=0.0)

    usuario = db.relationship('Usuario', backref='cierres_caja')

    def __repr__(self):
        return f'<CierreCaja {self.fecha} usuario {self.usuario_id}>'
