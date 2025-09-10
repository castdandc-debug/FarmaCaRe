# app/forms.py
from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField, SelectField, 
    FloatField, IntegerField, TextAreaField
)
from wtforms.validators import DataRequired, Length, Email, Optional, NumberRange

# --- Autenticación ---
class LoginForm(FlaskForm):
    nombre = StringField('Usuario', validators=[DataRequired(), Length(min=4, max=20)])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recordarme')
    submit = SubmitField('Iniciar Sesión')

# --- Usuario ---
class UsuarioForm(FlaskForm):
    nombre = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=4, max=100)])
    rol = SelectField('Rol', choices=[('Administrador', 'Administrador'), ('Caja', 'Caja')], validators=[DataRequired()])
    submit = SubmitField('Guardar')

# --- Cliente ---
class ClienteForm(FlaskForm):
    nombre = StringField('Nombre o Razón Social', validators=[DataRequired(), Length(max=150)])
    rfc = StringField('RFC', validators=[Optional(), Length(max=13)])
    direccion = StringField('Dirección', validators=[Optional(), Length(max=200)])
    telefono = StringField('Teléfono', validators=[Optional(), Length(max=15)])
    email = StringField('Correo Electrónico', validators=[Optional(), Email(), Length(max=100)])
    contacto = StringField('Contacto', validators=[Optional(), Length(max=150)])
    telefono_contacto = StringField('Teléfono de Contacto', validators=[Optional(), Length(max=15)])
    submit = SubmitField('Guardar')

# --- Proveedor ---
class ProveedorForm(FlaskForm):
    nombre = StringField('Nombre o Razón Social', validators=[DataRequired(), Length(max=150)])
    rfc = StringField('RFC', validators=[Optional(), Length(max=13)])
    direccion = StringField('Dirección', validators=[Optional(), Length(max=200)])
    telefono = StringField('Teléfono', validators=[Optional(), Length(max=15)])
    email = StringField('Correo Electrónico', validators=[Optional(), Email(), Length(max=100)])
    contacto = StringField('Contacto', validators=[Optional(), Length(max=150)])
    telefono_contacto = StringField('Teléfono de Contacto', validators=[Optional(), Length(max=15)])
    submit = SubmitField('Guardar')

# --- Medicamento ---
class MedicamentoForm(FlaskForm):
    codigo_barras = StringField('Código de Barras', validators=[DataRequired(), Length(max=50)])
    nombre_comercial = StringField('Nombre Comercial', validators=[DataRequired(), Length(max=150)])
    nombre_generico = StringField('Nombre Genérico', validators=[DataRequired(), Length(max=150)])
    laboratorio = StringField('Laboratorio/Casa Farmacéutica', validators=[DataRequired(), Length(max=100)])
    presentacion = StringField('Presentación', validators=[DataRequired(), Length(max=100)])
    grupo = SelectField('Grupo', choices=[
        ('I', 'Grupo I'),
        ('II', 'Grupo II'),
        ('III', 'Grupo III'),
        ('IV', 'Grupo IV'),
        ('V', 'Grupo V'),
        ('IV-Antibiotico', 'Grupo IV-Antibiótico')
    ], validators=[DataRequired()])
    iva = FloatField('IVA (%)', validators=[DataRequired(), NumberRange(min=0, max=100)], default=0.0)
    precio_venta = FloatField('Precio de Venta', validators=[DataRequired(), NumberRange(min=0)])
    punto_reorden = IntegerField('Punto de Reorden', validators=[Optional(), NumberRange(min=0)], default=10)
    submit = SubmitField('Guardar')

# --- Dispositivo Médico ---
class DispositivoMedicoForm(FlaskForm):
    codigo_barras = StringField('Código de Barras', validators=[DataRequired(), Length(max=50)])
    nombre_comercial = StringField('Nombre Comercial', validators=[DataRequired(), Length(max=150)])
    nombre_comun = StringField('Nombre Común', validators=[DataRequired(), Length(max=150)])
    laboratorio = StringField('Laboratorio/Marca', validators=[DataRequired(), Length(max=100)])
    presentacion = StringField('Presentación', validators=[DataRequired(), Length(max=100)])
    iva = FloatField('IVA (%)', validators=[DataRequired(), NumberRange(min=0, max=100)], default=0.0)
    precio_venta = FloatField('Precio de Venta', validators=[DataRequired(), NumberRange(min=0)])
    punto_reorden = IntegerField('Punto de Reorden', validators=[Optional(), NumberRange(min=0)], default=10)
    submit = SubmitField('Guardar')

# --- NoHay ---
class NoHayForm(FlaskForm):
    nombre = StringField('Nombre del Producto', validators=[DataRequired(), Length(max=100)])  # Ajustado a 100 por el modelo
    tipo = SelectField('Tipo', choices=[
        ('Poco inventario', 'Poco inventario'),
        ('No tiene el proveedor', 'No tiene el proveedor'),
        ('Descontinuado', 'Descontinuado'),
        ('No existe', 'No existe')
    ], validators=[DataRequired()])
    descripcion = TextAreaField('Descripción', validators=[Optional()])
    # usuario_id normalmente se asigna en la vista, pero se puede agregar un SelectField si necesitas elegir el usuario en el formulario.
    submit = SubmitField('Guardar')

# --- Ajuste de Inventario ---
class AjusteInventarioForm(FlaskForm):
    cantidad_ajustada = IntegerField('Cantidad de Ajuste', validators=[DataRequired()])
    motivo = StringField('Motivo del Ajuste', validators=[DataRequired(), Length(max=255)])
    submit = SubmitField('Realizar Ajuste')

# --- Venta ---
class VentaForm(FlaskForm):
    # El campo folio puede ser generado automáticamente, pero si quieres capturarlo manualmente:
    folio = IntegerField('Folio', validators=[Optional()])
    cliente_id = IntegerField('ID Cliente', validators=[Optional()])
    total = FloatField('Total', validators=[DataRequired(), NumberRange(min=0)])
    usuario_id = IntegerField('ID Usuario', validators=[Optional()])
    submit = SubmitField('Guardar')

# Puedes agregar más formularios según tus modelos y vistas.
