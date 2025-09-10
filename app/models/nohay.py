from app.extensions import db
from datetime import datetime

class NoHay(db.Model):
    __tablename__ = 'no_hay'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    usuario = db.relationship('Usuario')

    def __repr__(self):
        return f'<NoHay {self.nombre}>'
